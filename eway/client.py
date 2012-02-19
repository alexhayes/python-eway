import re
from decimal import Decimal
import xml.etree.cElementTree as ET

from httplib2 import Http
from urllib import urlencode, quote_plus

from eway import config
from eway.fields import Payment, Customer, Response

class EwayPaymentError(Exception): pass
    
class EwayPaymentClient(object):
    gateway_url = None
    customer_id = None
    transaction_data = {}
    
    def __init__(self, customer_id=config.EWAY_DEFAULT_CUSTOMER_ID, 
                       method=config.EWAY_DEFAULT_PAYMENT_METHOD, 
                       live_gateway=config.EWAY_DEFAULT_LIVE_GATEWAY,
                       pre_auth=False):
        
        self.customer_id = customer_id
        
        # FIXME: Clean up
        if method == config.REAL_TIME:
            if live_gateway:
                self.gateway_url = config.EWAY_PAYMENT_LIVE_REAL_TIME
            else:
                self.gateway_url = config.EWAY_PAYMENT_LIVE_REAL_TIME_TESTING_MODE
        elif method == config.REAL_TIME_CVN:
            if live_gateway:
                self.gateway_url = config.EWAY_PAYMENT_LIVE_REAL_TIME_CVN
            else:
                self.gateway_url = config.EWAY_PAYMENT_LIVE_REAL_TIME_CVN_TESTING_MODE
        elif method == config.STORED:
            self.gateway_url = config.EWAY_PAYMENT_STORED_LIVE
        elif method == config.GEO_IP_ANTI_FRAUD:
            if live_gateway:
                self.gateway_url = config.EWAY_PAYMENT_LIVE_GEO_IP_ANTI_FRAUD
            else:
                # in testing mode process with REAL-TIME
                self.gateway_url = config.EWAY_PAYMENT_LIVE_GEO_IP_ANTI_FRAUD_TESTING_MODE
        else:
            raise EwayPaymentError('Could not determine method: %s', (method))
    
    def get_reference(self, prefix=None):
        from datetime import datetime
        reference = datetime.now().strftime("%Y%m%d%H%M%S")
        if prefix:
            reference = prefix + reference
        return reference
    
    def authorisation(self, amount, credit_card, customer=None, reference=None):
        """
        Perform a pre-authorisation request.
        
        @param amount: The amount to charge
        @param credit_card: An instance of CreditCard
        @param customer: An instance of Customer
        @param reference: A reference for the transaction
        @return: An instance of Response
        
        @author: Alex Hayes <alex@alution.com>
        """
        if self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME:
            gateway_url = config.EWAY_PAYMENT_LIVE_AUTH
        elif self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_TESTING_MODE:
            gateway_url = config.EWAY_PAYMENT_LIVE_AUTH_TESTING_MODE
        elif self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_CVN:
            gateway_url = config.EWAY_PAYMENT_LIVE_AUTH_CVN
        elif self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_CVN_TESTING_MODE:
            gateway_url = config.EWAY_PAYMENT_LIVE_AUTH_CVN_TESTING_MODE
        elif self.gateway_url == config.EWAY_PAYMENT_STORED_LIVE:
            gateway_url = config.EWAY_PAYMENT_STORED_LIVE

        return self.prepare_transaction(gateway_url, amount, credit_card, customer, reference)
    
    def payment(self, amount, credit_card, customer=None, reference=None):
        """
        Perform a payment request.
        
        @param amount: The amount to charge
        @param credit_card: An instance of CreditCard
        @param customer: An instance of Customer
        @param reference: A reference for the transaction
        @return: An instance of Response
        
        @author: Alex Hayes <alex@alution.com>
        """
        return self.prepare_transaction(self.gateway_url, amount, credit_card, customer, reference)
    
    def prepare_transaction(self, gateway_url, amount, credit_card, customer=None, reference=None):
        """
        Prepare a payment request and send it to eWAY.
        
        @param gateway_url: The gateway url to use for the transaction
        @param amount: The amount to charge
        @param credit_card: An instance of CreditCard
        @param customer: An instance of Customer
        @param reference: A reference for the transaction
        @return: An instance of Response
        
        @author: Alex Hayes <alex@alution.com>
        """
        if not reference:
            prefix = credit_card.last_name
            prefix.replace(" ", "").lower()
            reference = self.get_reference(prefix)
            
        payment = Payment(total_amount=amount,
                          transaction_number=reference)
        
        data = payment.get_data()
        data.update(credit_card.get_data())

        if customer:
            data.update(customer.get_data())
        else:
            customer = Customer()
            data.update(customer.get_data())
        
        request_data = self.build_request(data)
        return self.send_transaction(gateway_url, request_data)
    
    def complete(self, amount, transaction_id, reference=None):
        """
        Complete an existing authorisation
        """
        if self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME or self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_CVN:
            gateway_url = config.EWAY_PAYMENT_LIVE_AUTH_COMPLETE
        elif self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_TESTING_MODE or self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_CVN_TESTING_MODE:
            gateway_url = config.EWAY_PAYMENT_LIVE_AUTH_COMPLETE_TESTING_MODE
        else:
            raise EwayPaymentError('Could not determine complete method: %s', (method))
        
        if not reference:
            reference = self.get_reference('')
            
        payment = Payment(total_amount=amount,
                          transaction_number=reference)
        
        data = payment.get_data()
        data['ewayAuthTrxnNumber'] = transaction_id
        data['ewayCardExpiryMonth'] = ''
        data['ewayCardExpiryYear'] = ''

        request_data = self.build_request(data)
        return self.send_transaction(gateway_url, request_data)
        
    def void(self, amount, transaction_id, reference=None):
        """
        Void an existing authorisation
        
        @param amount: The amount to void.
        """
        if self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME or self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_CVN:
            gateway_url = config.EWAY_PAYMENT_LIVE_AUTH_VOID
        elif self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_TESTING_MODE or self.gateway_url == config.EWAY_PAYMENT_LIVE_REAL_TIME_CVN_TESTING_MODE:
            gateway_url = config.EWAY_PAYMENT_LIVE_AUTH_VOID_TESTING_MODE
        else:
            raise EwayPaymentError('Could not determine complete method: %s', (method))
        
        if not reference:
            reference = self.get_reference('')
            
        payment = Payment(total_amount=amount,
                          transaction_number=reference)
        
        data = payment.get_data()
        data['ewayAuthTrxnNumber'] = transaction_id
        data['ewayCardExpiryMonth'] = ''
        data['ewayCardExpiryYear'] = ''

        request_data = self.build_request(data)
        return self.send_transaction(gateway_url, request_data)
    
    def build_request(self, data):
        root = ET.Element("ewaygateway")
        customer_element = ET.Element("ewayCustomerID")
        customer_element.text = str(self.customer_id)
        root.append(customer_element)
        
        for key, value in data.items():
            subelement = ET.Element(key)
            subelement.text = str(value)
            root.append(subelement)
        return ET.tostring(root)

    def send_transaction(self, gateway_url, xml):
        """
        Send XML Transaction Data and receive XML response
        
        @param gateway_url: The gateway url
        @param xml: The XML to send.
        @return: Instance of Response
        """
        headers = {
            'User-Agent': 'Python eWAY Payment Client',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        h = Http()
        response, content = h.request(gateway_url, "POST", xml, headers)

        if response.status != 200:
            raise EwayPaymentError('HTTP Error %s %d', (response.status, response.reason))

        response = Response()
        response.parse(content)
        return response

