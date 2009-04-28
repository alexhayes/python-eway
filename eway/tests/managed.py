from datetime import datetime
import sys
import unittest
from decimal import Decimal

sys.path.append("../..")

from eway.managed_client import *
from eway.managed_service_types import *


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.loc = ManagedCustomerLocator(live=False)
        self.svc = self.loc.get_managed_customer_service()
    
    def test_create_customer(self):
        customer = CreateCustomer()
        customer.title = "Mr." # "Mr., Ms., Mrs., Miss, Dr., Sir. or Prof."
        customer.first_name = "Joe"
        customer.last_name = "Bloggs"
        customer.company = "Test Company"
        customer.address = "test street"
        customer.suburb = "Sydney"
        customer.state = "NSW"
        customer.postcode = "2000"
        customer.country = "au" # must be lowercase
        
        customer.email = "test@eway.com.au"
        customer.url = "http://www.google.com.au"
        customer.mobile = "0404085992"
        customer.fax = "0267720000"
        customer.phone = "0267720000"
        
        customer.job_description = "test"
        customer.comments = "Now!"
        customer.customer_reference = "REF100"

        customer.card_number = "4444333322221111"
        customer.card_holder_name = "Test Account"
        customer.card_expiry_month = 1
        customer.card_expiry_year = 10
        
        response = self.svc.create_customer(customer)
        
        self.assertTrue(isinstance(response, CreateCustomerResponse))
        self.assertTrue(hasattr(response, "create_customer_result"))
        self.assertEqual(response.create_customer_result, "112233445566")
        
    def test_update_customer(self):
        customer = UpdateCustomer()
        customer.id = 9876543211000
        customer.title = "Mr." # "Mr., Ms., Mrs., Miss, Dr., Sir. or Prof."
        customer.first_name = "Joe"
        customer.last_name = "Bloggs"
        customer.company = "Test Company"
        customer.address = "test street"
        customer.suburb = "Sydney"
        customer.state = "NSW"
        customer.postcode = "2000"
        customer.country = "au" # must be lowercase
    
        
        customer.email = "test@eway.com.au"
        customer.url = "http://www.google.com.au"
        customer.mobile = "0404085992"
        customer.fax = "0267720000"
        customer.phone = "0267720000"
        
        customer.job_description = "test"
        customer.comments = "Now!"
        customer.customer_reference = "REF100"
    
        customer.card_number = "4444333322221111"
        customer.card_holder_name = "Test Account"
        customer.card_expiry_month = 1
        customer.card_expiry_year = 10
        
        response = self.svc.update_customer(customer)
        
        self.assertTrue(isinstance(response, UpdateCustomerResponse))
        self.assertTrue(hasattr(response, "update_customer_result"))
        self.assertEqual(response.update_customer_result, True)
        
    def test_query_customer(self):
        query_customer = QueryCustomer()
        query_customer.id = 9876543211000
        response = self.svc.query_customer(query_customer)
        
        self.assertTrue(isinstance(response, QueryCustomerResponse))
        self.assertTrue(hasattr(response, "query_customer_result"))
        customer_response = response.query_customer_result
        
        self.assertEqual(customer_response.id, 9876543211000)
        self.assertEqual(customer_response.reference, 'customer reference')
        self.assertEqual(customer_response.title, 'Mr.')
        self.assertEqual(customer_response.first_name, 'Jo')
        self.assertEqual(customer_response.last_name, 'Smith')
        self.assertEqual(customer_response.company, 'company')
        self.assertEqual(customer_response.job_description, '')
        self.assertEqual(customer_response.email, 'test@eway.com.au')
        self.assertEqual(customer_response.address, '15 Dundas Court')
        self.assertEqual(customer_response.suburb, 'phillip')
        self.assertEqual(customer_response.state, 'act')
        self.assertEqual(customer_response.postcode, '2606')
        self.assertEqual(customer_response.country, 'au')
        self.assertEqual(customer_response.phone1, '02111111111')
        self.assertEqual(customer_response.phone2, '04111111111')
        self.assertEqual(customer_response.fax, '111122222')
        self.assertEqual(customer_response.url, 'http://eway.com.au')
        self.assertEqual(customer_response.comments, 'Comments')
    
    def test_process_payment(self):
        process_payment = ProcessPayment()
        process_payment.id = 9876543211000
        process_payment.amount = 10.00
        process_payment.invoice_reference = ""
        process_payment.invoice_description = ""
        response = self.svc.process_payment(process_payment)
        
        self.assertTrue(isinstance(response, ProcessPaymentResponse))
        self.assertTrue(hasattr(response, "response"))
        
        payment_response = response.response
        
        self.assertEqual(payment_response.transaction_error, "10,Approved For Partial Amount(Test Gateway)")
        self.assertEqual(payment_response.transaction_status, 'True')
        self.assertNotEqual(payment_response.transaction_number, None)
        self.assertEqual(payment_response.return_amount, '10')
        self.assertEqual(payment_response.auth_code, '123456')
        
    def test_query_payment(self):
        payment_query = QueryPayment()
        payment_query.id = 9876543211000
        response = self.svc.query_payment(payment_query)
        
        self.assertTrue(isinstance(response, QueryPaymentResponse))
        self.assertTrue(hasattr(response, "query_payment_result"))
        payment_response = response.query_payment_result
        self.assertTrue(isinstance(payment_response.managed_transaction, list))
        
        today = datetime.today()
        
        for payment in payment_response.managed_transaction:
            self.assertTrue(payment.total_amount in [1000, 1008])
            self.assertEqual(payment.result, 1)
            self.assertEqual(payment.response_text, 'Approved')
            self.assertEqual(payment.transaction_date, (today.year, today.month, today.day, 0, 0, 0, 0, 0, 0))
            self.assertEqual(payment.transaction_number, 1)
        
    def test_query_customer_by_reference(self):
        query_customer = QueryCustomerByReference()
        query_customer.customer_reference = 'customer reference'
        response = self.svc.query_customer_by_reference(query_customer)
        self.assertTrue(isinstance(response, QueryCustomerByReferenceResponse))
        self.assertTrue(hasattr(response, "query_customer_by_reference_result"))
        self.assertEqual(response.query_customer_by_reference_result, None)


if __name__ == '__main__':
    unittest.main()
