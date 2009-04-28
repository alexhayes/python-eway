from ZSI import client

from managed_service_types import *

class ManagedCustomerLocator(object):
    def __init__(self, url=None, live=True):
        if not url:
            if live:
                self.soap_address = "https://www.eway.com.au/gateway/ManagedPaymentService/managedCreditCardPayment.asmx"
            else:
                self.soap_address = "https://www.eway.com.au/gateway/ManagedPaymentService/test/managedCreditCardPayment.asmx"
        else:
            self.soap_address = url
            
    def get_managed_customer_service(self, url=None, **kwargs):
        return ManagedCustomerService(url or self.soap_address, **kwargs)


class ManagedCustomerService(object):
    def __init__(self, url, customer_id=None, username=None, password=None, binding=None):
        self.customer_id = customer_id or 87654321
        self.username = username or 'test@eway.com.au'
        self.password = password or 'test123'
        
        if binding:
            self.binding = binding
        else:
            self.binding = client.Binding(url=url)

    def get_soap_headers(self):
        EwayHeader = Eway.EwayHeader().pyclass
        eway_header = EwayHeader()
        eway_header.customer_id = self.customer_id
        eway_header.username = self.username
        eway_header.password = self.password
        return [eway_header]

    def create_customer(self, request, **kwargs):
        if not isinstance(request, CreateCustomer):
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        kwargs.setdefault("soapheaders", self.get_soap_headers())
        self.binding.Send(None, None, request, soapaction="https://www.eway.com.au/gateway/managedpayment/CreateCustomer", **kwargs)
        # no output wsaction
        response = self.binding.Receive(CreateCustomerResponse.typecode)
        return response

    def update_customer(self, request, **kwargs):
        if not isinstance(request, UpdateCustomer):
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        kwargs.setdefault("soapheaders", self.get_soap_headers())
        self.binding.Send(None, None, request, soapaction="https://www.eway.com.au/gateway/managedpayment/UpdateCustomer", **kwargs)
        # no output wsaction
        response = self.binding.Receive(UpdateCustomerResponse.typecode)
        return response

    def query_customer(self, request, **kwargs):
        if not isinstance(request, QueryCustomer):
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        kwargs.setdefault("soapheaders", self.get_soap_headers())
        self.binding.Send(None, None, request, soapaction="https://www.eway.com.au/gateway/managedpayment/QueryCustomer", **kwargs)
        # no output wsaction
        response = self.binding.Receive(QueryCustomerResponse.typecode)
        return response

    def query_customer_by_reference(self, request, **kwargs):
        if not isinstance(request, QueryCustomerByReference):
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        kwargs.setdefault("soapheaders", self.get_soap_headers())
        self.binding.Send(None, None, request, soapaction="https://www.eway.com.au/gateway/managedpayment/QueryCustomerByReference", **kwargs)
        # no output wsaction
        response = self.binding.Receive(QueryCustomerByReferenceResponse.typecode)
        return response

    def process_payment(self, request, **kwargs):
        if not isinstance(request, ProcessPayment):
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        kwargs.setdefault("soapheaders", self.get_soap_headers())
        self.binding.Send(None, None, request, soapaction="https://www.eway.com.au/gateway/managedpayment/ProcessPayment", **kwargs)
        # no output wsaction
        response = self.binding.Receive(ProcessPaymentResponse.typecode)
        return response

    def query_payment(self, request, **kwargs):
        if not isinstance(request, QueryPayment):
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        kwargs.setdefault("soapheaders", self.get_soap_headers())
        self.binding.Send(None, None, request, soapaction="https://www.eway.com.au/gateway/managedpayment/QueryPayment", **kwargs)
        # no output wsaction
        response = self.binding.Receive(QueryPaymentResponse.typecode)
        return response

CreateCustomer = Eway.CreateCustomer().pyclass
CreateCustomerResponse = Eway.CreateCustomerResponse().pyclass

UpdateCustomer = Eway.UpdateCustomer().pyclass
UpdateCustomerResponse = Eway.UpdateCustomerResponse().pyclass

QueryCustomer = Eway.QueryCustomer().pyclass
QueryCustomerResponse = Eway.QueryCustomerResponse().pyclass

QueryCustomerByReference = Eway.QueryCustomerByReference().pyclass
QueryCustomerByReferenceResponse = Eway.QueryCustomerByReferenceResponse().pyclass

ProcessPayment = Eway.ProcessPayment().pyclass
ProcessPaymentResponse = Eway.ProcessPaymentResponse().pyclass

QueryPayment = Eway.QueryPayment().pyclass
QueryPaymentResponse = Eway.QueryPaymentResponse().pyclass
