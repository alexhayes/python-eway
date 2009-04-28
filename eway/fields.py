import xml.etree.cElementTree as ET

from validate import Validator, Field, CentsField

class Response(Validator):
    amount = Field("ewayTrxnAmount")
    transaction_number = Field("ewayTrxnTransactionNumber")
    invoice_reference = Field("ewayTrxnInvoiceReference")
    status = Field("ewayTrxnStatus")
    auth_code = Field("ewayTrxnAuthCode")
    error = Field("ewayTrxnError")
    
    option1 = Field("ewayTrxnOption1")
    option2 = Field("ewayTrxnOption2")
    option3 = Field("ewayTrxnOption3")
    
    success_codes = ['16', '11', '10', '08', '00']
    
    def parse(self, xml):
        tree = ET.fromstring(xml)
        for key, field in self.fields.items():
            setattr(self, key, tree.findtext(field.external_name))
    
    @property      
    def success(self):
        return self.status.lower() == 'true'
                

class Customer(Validator):
    first_name = Field("ewayCustomerFirstName", default="")
    last_name = Field("ewayCustomerLastName", default="")
    email = Field("ewayCustomerEmail", default="")
    address = Field("ewayCustomerAddress", default="")
    postcode = Field("ewayCustomerPostcode", default="")
    invoice_description = Field("ewayCustomerInvoiceDescription", default="")
    invoice_reference = Field("ewayCustomerInvoiceRef", default="")
    country = Field("ewayCustomerBillingCountry", default="")
    ip_address = Field("ewayCustomerIPAddress", default="")


class CreditCard(Validator):
    holder_name = Field("ewayCardHoldersName")
    number = Field("ewayCardNumber")
    expiry_month = Field("ewayCardExpiryMonth")
    expiry_year = Field("ewayCardExpiryYear")
    verification_number = Field("ewayCVN")


class Payment(Validator):
    total_amount = CentsField("ewayTotalAmount")
    transaction_number = Field("ewayTrxnNumber")
    # Magic Variables
    option1 = Field("ewayOption1", default="")
    option2 = Field("ewayOption2", default="")
    option3 = Field("ewayOption3", default="")