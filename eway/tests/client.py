import sys
import unittest
from decimal import Decimal

sys.path.insert(0, "./../../")

from eway import config
from eway.client import EwayPaymentClient
from eway.fields import Customer, CreditCard

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.eway_client = EwayPaymentClient('87654321',
                                             config.REAL_TIME_CVN,
                                             False)
    
    def get_data(self):
        """
        Test the eWAY auth complete functionality.
        """
        customer = Customer()
        customer.first_name = "Joe"
        customer.last_name = "Bloggs"
        customer.email = "name@xyz.com.au"
        customer.address = "123 Someplace Street, Somewhere ACT"
        customer.postcode = "2609"
        customer.invoice_description = "Testing"
        customer.invoice_reference = "INV120394"
        customer.country = "AU"

        credit_card = CreditCard()
        credit_card.holder_name = '%s %s' % (customer.first_name, customer.last_name,)
        credit_card.number = "4444333322221111" 
        credit_card.expiry_month = 10
        credit_card.expiry_year = 12
        credit_card.verification_number = "123"
        credit_card.ip_address = "127.0.0.1"
        
        return [customer, credit_card]
    
    def test_payment(self):
        """
        Test the eWAY payment functionality.
        """
        customer, credit_card = self.get_data()

        if customer.is_valid() and credit_card.is_valid():
            response = self.eway_client.payment(
                Decimal("10.08"), 
                credit_card=credit_card, 
                customer=customer, 
                reference="123456"
            )
            self.failUnless(response.success)
            self.failUnlessEqual('Honour With Identification(Test CVN Gateway)', response.get_message())
            self.failUnlessEqual('08', response.get_code(), 'Response code should be 08')

    def test_authorisation_complete(self):
        """
        Test the eWAY auth complete functionality.
        
        @author: Alex Hayes <alex@alution.com> 
        """
        customer, credit_card = self.get_data()

        if customer.is_valid() and credit_card.is_valid():
            amount = Decimal("10.00")
            
            response = self.eway_client.authorisation(
                amount, 
                credit_card=credit_card, 
                customer=customer, 
                reference="123456"
            )
            self.failUnless(response.success)
            self.failUnlessEqual('Transaction Approved(Test CVN Gateway)', response.get_message())
            self.failUnlessEqual('00', response.get_code(), 'Response code should be 00')
            
            response = self.eway_client.complete(
                amount,
                10000000 # eWAY's test transaction number - response.transaction_number, 
            )
            self.failUnless(response.success)
            """
            In the following note the lack of CVN, according to eWAY this is because there is no CVN gateway for auth or void.
            """
            self.failUnlessEqual('Transaction Approved(Test Gateway)', response.get_message())
            self.failUnlessEqual('00', response.get_code(), 'Response code should be 00')
        
    def test_authorisation_void(self):
        """
        Test the eWAY auth void functionality.
        
        @author: Alex Hayes <alex@alution.com> 
        """
        customer, credit_card = self.get_data()

        if customer.is_valid() and credit_card.is_valid():
            amount = Decimal("10.00")
            
            response = self.eway_client.authorisation(
                amount, 
                credit_card=credit_card, 
                customer=customer, 
                reference="123456"
            )
            self.failUnless(response.success)
            self.failUnlessEqual('Transaction Approved(Test CVN Gateway)', response.get_message())
            self.failUnlessEqual('00', response.get_code(), 'Response code should be 00')
            
            response = self.eway_client.void(
                amount,
                10000000 # eWAY's test transaction number - response.transaction_number, 
            )
            self.failUnless(response.success)
            """
            In the following note the lack of CVN, according to eWAY this is because there is no CVN gateway for auth or void.
            """
            self.failUnlessEqual('Transaction Approved(Test Gateway)', response.get_message())
            self.failUnlessEqual('00', response.get_code(), 'Response code should be 00')
        
        

if __name__ == '__main__':
    unittest.main()

