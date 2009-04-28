import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED

################################################
# targetNamespace
# https://www.eway.com.au/gateway/managedpayment
################################################

class Eway:
    targetNamespace = "https://www.eway.com.au/gateway/managedpayment"

    class EwayHeader(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "https://www.eway.com.au/gateway/managedpayment"
        type = (schema, "eWAYHeader")
        def __init__(self, pname=None, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = Eway.eWAYHeader.schema
            TClist = [ZSI.TC.String(pname=(ns,"eWAYCustomerID"), aname="customer_id", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Username"), aname="username", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Password"), aname="password", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            else:
                # attribute handling code
                self.attribute_typecode_dict[("http://www.w3.org/2001/XMLSchema","anyAttribute")] = ZSI.TC.AnyElement()
            
            if not pname:
                pname = ("https://www.eway.com.au/gateway/managedpayment","eWAYHeader")
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._eWAYCustomerID = None
                    self._Username = None
                    self._Password = None
                    return
            Holder.__name__ = "eWAYHeader_Holder"
            self.pyclass = Holder

    class CreditCard(TypeDefinition):
        #complexType/complexContent extension
        schema = "https://www.eway.com.au/gateway/managedpayment"
        type = (schema, "CreditCard")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ns = Eway.CreditCard.schema
            TClist = [ZSI.TC.String(pname=(ns,"CCName"), aname="name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CCNumber"), aname="number", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CCExpiryMonth"), aname="expiry_month", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CCExpiryYear"), aname="expiry_year", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            attributes = self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            if Eway.ManagedCustomer not in Eway.CreditCard.__bases__:
                bases = list(Eway.CreditCard.__bases__)
                bases.insert(0, Eway.ManagedCustomer)
                Eway.CreditCard.__bases__ = tuple(bases)

            Eway.ManagedCustomer.__init__(self, pname, ofwhat=TClist, extend=True, attributes=attributes, **kw)

    class ManagedCustomer(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "https://www.eway.com.au/gateway/managedpayment"
        type = (schema, "ManagedCustomer")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = Eway.ManagedCustomer.schema
            TClist = [ZSI.TCnumbers.Ilong(pname=(ns,"ManagedCustomerID"), aname="id", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerRef"), aname="reference", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerTitle"), aname="title", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerFirstName"), aname="first_name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerLastName"), aname="last_name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerCompany"), aname="company", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerJobDesc"), aname="job_description", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerEmail"), aname="email", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerAddress"), aname="address", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerSuburb"), aname="suburb", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerState"), aname="state", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerPostCode"), aname="postcode", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerCountry"), aname="country", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerPhone1"), aname="phone1", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerPhone2"), aname="phone2", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerFax"), aname="fax", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerURL"), aname="url", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerComments"), aname="comments", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.id = None
                    self.reference = None
                    self.title = None
                    self.first_name = None
                    self.last_name = None
                    self.company = None
                    self.job_description = None
                    self.email = None
                    self.address = None
                    self.suburb = None
                    self.state = None
                    self.postcode = None
                    self.country = None
                    self.phone1 = None
                    self.phone2 = None
                    self.fax = None
                    self.url = None
                    self.comments = None
                    return
            Holder.__name__ = "ManagedCustomer_Holder"
            self.pyclass = Holder

    class CCPaymentResponse(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "https://www.eway.com.au/gateway/managedpayment"
        type = (schema, "CCPaymentResponse")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = Eway.CCPaymentResponse.schema
            TClist = [ZSI.TC.String(pname=(ns,"ewayTrxnError"), aname="transaction_error", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"ewayTrxnStatus"), aname="transaction_status", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"ewayTrxnNumber"), aname="transaction_number", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"ewayReturnAmount"), aname="return_amount", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"ewayAuthCode"), aname="auth_code", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.transaction_erro = None
                    self.transaction_status = None
                    self.transaction_number = None
                    self.return_amount = None
                    self.auth_code = None
                    return
            Holder.__name__ = "CCPaymentResponse_Holder"
            self.pyclass = Holder

    class ArrayOfManagedTransaction(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "https://www.eway.com.au/gateway/managedpayment"
        type = (schema, "ArrayOfManagedTransaction")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = Eway.ArrayOfManagedTransaction.schema
            TClist = [GTD("https://www.eway.com.au/gateway/managedpayment","ManagedTransaction",lazy=False)(pname=(ns,"ManagedTransaction"), aname="managed_transaction", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.managed_transaction = []
                    return
            Holder.__name__ = "ArrayOfManagedTransaction_Holder"
            self.pyclass = Holder

    class ManagedTransaction(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "https://www.eway.com.au/gateway/managedpayment"
        type = (schema, "ManagedTransaction")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = Eway.ManagedTransaction.schema
            TClist = [ZSI.TCnumbers.Iint(pname=(ns,"TotalAmount"), aname="total_amount", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TCnumbers.Iint(pname=(ns,"Result"), aname="result", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"ResponseText"), aname="response_text", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TCtimes.gDateTime(pname=(ns,"TransactionDate"), aname="transaction_date", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TCnumbers.Iint(pname=(ns,"ewayTrxnNumber"), aname="transaction_number", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.total_amount = None
                    self.result = None
                    self.response_text = None
                    self.transaction_date = None
                    self.transaction_number = None
                    return
            Holder.__name__ = "ManagedTransaction_Holder"
            self.pyclass = Holder

    class CreateCustomer(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "CreateCustomer"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.CreateCustomer.schema
            TClist = [ZSI.TC.String(pname=(ns,"Title"), aname="title", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")),
                     ZSI.TC.String(pname=(ns,"FirstName"), aname="first_name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"LastName"), aname="last_name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Address"), aname="address", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Suburb"), aname="suburb", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"State"), aname="state", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Company"), aname="company", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"PostCode"), aname="postcode", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Country"), aname="country", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Email"), aname="email", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Fax"), aname="fax", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Phone"), aname="phone", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Mobile"), aname="mobile", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"CustomerRef"), aname="customer_reference", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"JobDesc"), aname="job_description", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"Comments"), aname="comments", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"URL"), aname="url", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"CCNumber"), aname="card_number", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TC.String(pname=(ns,"CCNameOnCard"), aname="card_holder_name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TCnumbers.Iint(pname=(ns,"CCExpiryMonth"), aname="card_expiry_month", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                     ZSI.TCnumbers.Iint(pname=(ns,"CCExpiryYear"), aname="card_expiry_year", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","CreateCustomer")
            kw["aname"] = "_CreateCustomer"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    self.title = None
                    self.first_name = None
                    self.last_name = None
                    self.address = None
                    self.suburb = None
                    self.state = None
                    self.company = None
                    self.postcode = None
                    self.company = None
                    self.email = None
                    self.fax = None
                    self.phone = None
                    self.mobile = None
                    self.customer_reference = None
                    self.job_description = None
                    self.comments = None
                    self.url = None
                    self.card_number = None
                    self.card_holder_name = None
                    self.card_expiry_month = None
                    self.card_expiry_year = None
                    return
            Holder.__name__ = "CreateCustomer_Holder"
            self.pyclass = Holder

    class CreateCustomerResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "CreateCustomerResponse"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.CreateCustomerResponse.schema
            TClist = [ZSI.TC.String(pname=(ns,"CreateCustomerResult"), aname="create_customer_result", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","CreateCustomerResponse")
            kw["aname"] = "_CreateCustomerResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    self.create_customer_result = None
                    return
            Holder.__name__ = "CreateCustomerResponse_Holder"
            self.pyclass = Holder

    class eWAYHeader(ElementDeclaration):
        literal = "eWAYHeader"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","eWAYHeader")
            kw["aname"] = "_eWAYHeader"
            if Eway.eWAYHeader not in Eway.eWAYHeader.__bases__:
                bases = list(Eway.eWAYHeader.__bases__)
                bases.insert(0, Eway.eWAYHeader)
                Eway.eWAYHeader.__bases__ = tuple(bases)

            Eway.eWAYHeader.__init__(self, **kw)
            if self.pyclass is not None: self.pyclass.__name__ = "eWAYHeader_Holder"

    class UpdateCustomer(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "UpdateCustomer"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.UpdateCustomer.schema
            TClist = [ZSI.TCnumbers.Ilong(pname=(ns,"managedCustomerID"), aname="id", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Title"), aname="title", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"FirstName"), aname="first_name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"LastName"), aname="last_name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Address"), aname="address", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Suburb"), aname="suburb", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"State"), aname="state", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Company"), aname="company", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"PostCode"), aname="postcode", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Country"), aname="country", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Email"), aname="email", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Fax"), aname="fax", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Phone"), aname="phone", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Mobile"), aname="mobile", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CustomerRef"), aname="customer_reference", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"JobDesc"), aname="job_description", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"Comments"), aname="comments", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"URL"), aname="url", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CCNumber"), aname="card_number", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"CCNameOnCard"), aname="card_holder_name", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TCnumbers.Iint(pname=(ns,"CCExpiryMonth"), aname="card_expiry_month", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TCnumbers.Iint(pname=(ns,"CCExpiryYear"), aname="card_expiry_year", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","UpdateCustomer")
            kw["aname"] = "_UpdateCustomer"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.id = None
                    self.title = None
                    self.first_name = None
                    self.last_name = None
                    self.address = None
                    self.suburb = None
                    self.state = None
                    self.company = None
                    self.postcode = None
                    self.country = None
                    self.email = None
                    self.fax = None
                    self.phone = None
                    self.mobile = None
                    self.customer_reference = None
                    self.job_description = None
                    self.comments = None
                    self.url = None
                    self.card_number = None
                    self.card_holder_name = None
                    self.card_expiry_month = None
                    self.card_expiry_year = None
                    return
            Holder.__name__ = "UpdateCustomer_Holder"
            self.pyclass = Holder

    class UpdateCustomerResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "UpdateCustomerResponse"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.UpdateCustomerResponse.schema
            TClist = [ZSI.TC.Boolean(pname=(ns,"UpdateCustomerResult"), aname="update_customer_result", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","UpdateCustomerResponse")
            kw["aname"] = "update_customer_response"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.update_customer_result = None
                    return
            Holder.__name__ = "UpdateCustomerResponse_Holder"
            self.pyclass = Holder

    class QueryCustomer(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "QueryCustomer"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.QueryCustomer.schema
            TClist = [ZSI.TCnumbers.Ilong(pname=(ns,"managedCustomerID"), aname="id", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","QueryCustomer")
            kw["aname"] = "_QueryCustomer"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.id = None
                    return
            Holder.__name__ = "QueryCustomer_Holder"
            self.pyclass = Holder

    class QueryCustomerResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "QueryCustomerResponse"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.QueryCustomerResponse.schema
            TClist = [GTD("https://www.eway.com.au/gateway/managedpayment","CreditCard",lazy=False)(pname=(ns,"QueryCustomerResult"), aname="query_customer_result", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","QueryCustomerResponse")
            kw["aname"] = "_QueryCustomerResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.query_customer_result = None
                    return
            Holder.__name__ = "QueryCustomerResponse_Holder"
            self.pyclass = Holder

    class QueryCustomerByReference(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "QueryCustomerByReference"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.QueryCustomerByReference.schema
            TClist = [ZSI.TC.String(pname=(ns,"CustomerReference"), aname="customer_reference", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","QueryCustomerByReference")
            kw["aname"] = "_QueryCustomerByReference"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.customer_reference = None
                    return
            Holder.__name__ = "QueryCustomerByReference_Holder"
            self.pyclass = Holder

    class QueryCustomerByReferenceResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "QueryCustomerByReferenceResponse"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.QueryCustomerByReferenceResponse.schema
            TClist = [GTD("https://www.eway.com.au/gateway/managedpayment","CreditCard",lazy=False)(pname=(ns,"QueryCustomerByReferenceResult"), aname="query_customer_by_reference_result", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","QueryCustomerByReferenceResponse")
            kw["aname"] = "_QueryCustomerByReferenceResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.query_customer_by_reference_result = None
                    return
            Holder.__name__ = "QueryCustomerByReferenceResponse_Holder"
            self.pyclass = Holder

    class ProcessPayment(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "ProcessPayment"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.ProcessPayment.schema
            TClist = [ZSI.TCnumbers.Ilong(pname=(ns,"managedCustomerID"), aname="id", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TCnumbers.Iint(pname=(ns,"amount"), aname="amount", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"invoiceReference"), aname="invoice_reference", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), 
                      ZSI.TC.String(pname=(ns,"invoiceDescription"), aname="invoice_description", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","ProcessPayment")
            kw["aname"] = "_ProcessPayment"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.id = None
                    self.amount = None
                    self.invoice_reference = None
                    self.invoice_description = None
                    return
            Holder.__name__ = "ProcessPayment_Holder"
            self.pyclass = Holder

    class ProcessPaymentResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "ProcessPaymentResponse"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.ProcessPaymentResponse.schema
            TClist = [GTD("https://www.eway.com.au/gateway/managedpayment","CCPaymentResponse",lazy=False)(pname=(ns,"ewayResponse"), aname="response", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","ProcessPaymentResponse")
            kw["aname"] = "_ProcessPaymentResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.response = None
                    return
            Holder.__name__ = "ProcessPaymentResponse_Holder"
            self.pyclass = Holder

    class QueryPayment(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "QueryPayment"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.QueryPayment.schema
            TClist = [ZSI.TCnumbers.Ilong(pname=(ns,"managedCustomerID"), aname="id", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","QueryPayment")
            kw["aname"] = "_QueryPayment"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.id = None
                    return
            Holder.__name__ = "QueryPayment_Holder"
            self.pyclass = Holder

    class QueryPaymentResponse(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "QueryPaymentResponse"
        schema = "https://www.eway.com.au/gateway/managedpayment"
        def __init__(self, **kw):
            ns = Eway.QueryPaymentResponse.schema
            TClist = [GTD("https://www.eway.com.au/gateway/managedpayment","ArrayOfManagedTransaction",lazy=False)(pname=(ns,"QueryPaymentResult"), aname="query_payment_result", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("https://www.eway.com.au/gateway/managedpayment","QueryPaymentResponse")
            kw["aname"] = "_QueryPaymentResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self.query_payment_result = None
                    return
            Holder.__name__ = "QueryPaymentResponse_Holder"
            self.pyclass = Holder
