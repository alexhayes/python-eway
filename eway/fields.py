import xml.etree.cElementTree as ET
import re

from validate import Validator, Field, CentsField

class Response(Validator):
    """
    An eWAY response.
    
    Warning !!!:
    
    For property trxnReference, note that this is the field ewayTrxnNumber sent in the request to eway whereas
    self::getTrxnNumber() returns eWAY's own unique Transaction number.
    
    This information is contained in eWAY's own documentation: http://www.eway.com.au/Support/Developer/PaymentsRealTime.aspx
    
    This value is returned from the server to the client. You can pass a unique transaction number
    from your site. You can update and track the status of a transaction when eWAY
    returns to your site.
    
    NB. This number is returned as 'ewayTrxnReference'. The number returned as
    'ewayTrxnNumber', is actually the unique eWAY Transaction number, created by
    eWAY itself.
    
    @todo: Should probably make some attempt to normalise the input/output even tho
           it would go against eWAY's docs it would make much more sense to the user.
    """
    amount = Field("ewayTrxnAmount")
    transaction_number = Field("ewayTrxnNumber")
    transaction_reference = Field("ewayTrxnReference")
    status = Field("ewayTrxnStatus")
    auth_code = Field("ewayTrxnAuthCode")
    error = Field("ewayTrxnError")
    
    option1 = Field("ewayTrxnOption1")
    option2 = Field("ewayTrxnOption2")
    option3 = Field("ewayTrxnOption3")
    
    success_codes = ['16', '11', '10', '08', '00']

    # See http://www.eway.com.au/Developer/Downloads/ResponseCodes.aspx
    response_codes = {
        '00': 'Transaction Approved',
        '01': 'Refer to Issuer',
        '02': 'Refer to Issuer, special',
        '03': 'No Merchant',
        '04': 'Pick Up Card',
        '05': 'Do Not Honour',
        '06': 'Error',
        '07': 'Pick Up Card, Special',
        '08': 'Honour With Identification',
        '09': 'Request In Progress',
        '10': 'Approved For Partial Amount',
        '11': 'Approved, VIP',
        '12': 'Invalid Transaction',
        '13': 'Invalid Amount',
        '14': 'Invalid Card Number',
        '15': 'No Issuer',
        '16': 'Approved, Update Track 3',
        '19': 'Re-enter Last Transaction',
        '21': 'No Action Taken',
        '22': 'Suspected Malfunction',
        '23': 'Unacceptable Transaction Fee',
        '25': 'Unable to Locate Record On File',
        '30': 'Format Error',
        '31': 'Bank Not Supported By Switch',
        '33': 'Expired Card, Capture',
        '34': 'Suspected Fraud, Retain Card',
        '35': 'Card Acceptor, Contact Acquirer, Retain Card',
        '36': 'Restricted Card, Retain Card',
        '37': 'Contact Acquirer Security Department, Retain Card',
        '38': 'PIN Tries Exceeded, Capture',
        '39': 'No Credit Account',
        '40': 'Function Not Supported',
        '41': 'Lost Card',
        '42': 'No Universal Account',
        '43': 'Stolen Card',
        '44': 'No Investment Account',
        '51': 'Insufficient Funds',
        '52': 'No Cheque Account',
        '53': 'No Savings Account',
        '54': 'Expired Card',
        '55': 'Incorrect PIN',
        '56': 'No Card Record',
        '57': 'Function Not Permitted to Cardholder',
        '58': 'Function Not Permitted to Terminal',
        '59': 'Suspected Fraud',
        '60': 'Acceptor Contact Acquirer',
        '61': 'Exceeds Withdrawal Limit',
        '62': 'Restricted Card',
        '63': 'Security Violation',
        '64': 'Original Amount Incorrect',
        '66': 'Acceptor Contact Acquirer, Security',
        '67': 'Capture Card',
        '75': 'PIN Tries Exceeded',
        '82': 'CVV Validation Error',
        '90': 'Cutoff In Progress',
        '91': 'Card Issuer Unavailable',
        '92': 'Unable To Route Transaction',
        '93': 'Cannot Complete, Violation Of The Law',
        '94': 'Duplicate Transaction',
        '96': 'System Error',
    }
    
    def parse(self, xml):
        tree = ET.fromstring(xml)
        for key, field in self.fields.items():
            setattr(self, key, tree.findtext(field.external_name))
    
    @property      
    def success(self):
        return self.status.lower() == 'true'

    def get_code(self):
        """
        Retrieve the eWAY response code, contained within the error text or None
        """
        if re.match("[0-9]{2}", self.error):
            return self.error[:2]
        return None

    def get_message(self):
        """
        Retrieves a cleaned version of the eWAY response message.
        
        Note the following is performed:
            - If get_code returns true then everything after the response code is returned
            - strips the word eWAY out of the response
        """
        message = self.error

        if self.get_code():
            message = message[3:]

        # in testing appears like a regex replace is not necessary.
        return message.replace('eWAY ', '')
                

class Customer(Validator):
    first_name = Field("ewayCustomerFirstName", "First Name", default="")
    last_name = Field("ewayCustomerLastName", "Last Name", default="")
    email = Field("ewayCustomerEmail", "Email", default="")
    address = Field("ewayCustomerAddress", "Address", default="")
    postcode = Field("ewayCustomerPostcode", "Postcode", default="")
    invoice_description = Field("ewayCustomerInvoiceDescription", "Invoice Description", default="")
    invoice_reference = Field("ewayCustomerInvoiceRef", "Invoice Reference", default="")
    country = Field("ewayCustomerBillingCountry", "Country", default="")
    ip_address = Field("ewayCustomerIPAddress", "IP Address", default="")


class CreditCard(Validator):
    holder_name = Field("ewayCardHoldersName", "Card Holders Name")
    number = Field("ewayCardNumber", "Card Number")
    expiry_month = Field("ewayCardExpiryMonth", "Expiry Month")
    expiry_year = Field("ewayCardExpiryYear", "Expiry Year")
    verification_number = Field("ewayCVN", "CVN Number", required=False)


class Payment(Validator):
    total_amount = CentsField("ewayTotalAmount", "Total Amount")
    transaction_number = Field("ewayTrxnNumber", "Transaction Number")
    # Magic Variables
    option1 = Field("ewayOption1", default="")
    option2 = Field("ewayOption2", default="")
    option3 = Field("ewayOption3", default="")