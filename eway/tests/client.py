import sys
import unittest
from decimal import Decimal

sys.path.append("../..")

from eway import config
from eway.client import EwayPaymentClient
from eway.fields import Customer, CreditCard


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.eway_client = EwayPaymentClient('87654321',
                                             config.REAL_TIME_CVN,
                                             False)
    
    def test_client(self):
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

        if customer.is_valid() and credit_card.is_valid():
            response = self.eway_client.authorize(Decimal("10.08"), 
                                  credit_card=credit_card, 
                                  customer=customer, reference="123456")
            self.failUnless(response.success)

if __name__ == '__main__':
    unittest.main()

