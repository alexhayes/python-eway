import re
from decimal import Decimal
import xml.etree.cElementTree as ET

from httplib2 import Http
from urllib import urlencode, quote_plus

import config
from fields import Payment, Customer, Response

class EwayPaymentError(Exception): pass
    
class EwayPaymentClient(object):
    gateway_url = None
    customer_id = None
    transaction_data = {}
    
    def __init__(self, customer_id=config.EWAY_DEFAULT_CUSTOMER_ID, 
                       method=config.EWAY_DEFAULT_PAYMENT_METHOD, 
                       live_gateway=config.EWAY_DEFAULT_LIVE_GATEWAY):
        
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
            self.gateway_url = config.EWAY_STORED_LIVE
        elif method == config.GEO_IP_ANTI_FRAUD:
            if live_gateway:
                self.gateway_url = config.EWAY_PAYMENT_LIVE_GEO_IP_ANTI_FRAUD
            else:
                # in testing mode process with REAL-TIME
                self.gateway_url = config.EWAY_PAYMENT_LIVE_GEO_IP_ANTI_FRAUD_TESTING_MODE
    
    def get_reference(self, prefix=None):
        from datetime import datetime
        reference = datetime.now().strftime("%H%M%S%d%m%y")
        if prefix:
            reference = prefix + reference
        return reference
        
    def authorize(self, amount, credit_card, customer=None, reference=None):
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
        return self.send_transaction(request_data)
        
    
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

    def send_transaction(self, xml):
        """
        Send XML Transaction Data and receive XML response
        """
        headers = {
            'User-Agent': 'Python eWAY Payment Client',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        h = Http()
        response, content = h.request(self.gateway_url, "POST", xml, headers)

        if response.status != 200:
            raise EwayPaymentError('HTTP Error %s %d', (response.status, response.reason))

        response = Response()
        response.parse(content)
        return response

