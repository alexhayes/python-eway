# define script constants
REAL_TIME = 'REAL-TIME'
REAL_TIME_CVN = 'REAL-TIME-CVN'
GEO_IP_ANTI_FRAUD = 'GEO-IP-ANTI-FRAUD'
STORED = 'STORED'

# define URLs for payment gateway
EWAY_PAYMENT_LIVE_REAL_TIME = 'https://www.eway.com.au/gateway/xmlpayment.asp'
EWAY_PAYMENT_LIVE_REAL_TIME_TESTING_MODE = 'https://www.eway.com.au/gateway/xmltest/testpage.asp'
EWAY_PAYMENT_LIVE_REAL_TIME_CVN = 'https://www.eway.com.au/gateway_cvn/xmlpayment.asp'
EWAY_PAYMENT_LIVE_REAL_TIME_CVN_TESTING_MODE = 'https://www.eway.com.au/gateway_cvn/xmltest/testpage.asp'
EWAY_PAYMENT_LIVE_GEO_IP_ANTI_FRAUD = 'https://www.eway.com.au/gateway_beagle/xmlbeagle.asp'
EWAY_PAYMENT_LIVE_GEO_IP_ANTI_FRAUD_TESTING_MODE = 'https://www.eway.com.au/gateway_beagle/test/xmlbeagle_test.asp' # in testing mode process with REAL-TIME
EWAY_PAYMENT_HOSTED_REAL_TIME = 'https://www.eway.com.au/gateway/payment.asp'
EWAY_PAYMENT_HOSTED_REAL_TIME_TESTING_MODE = 'https://www.eway.com.au/gateway/payment.asp'
EWAY_PAYMENT_HOSTED_REAL_TIME_CVN = 'https://www.eway.com.au/gateway_cvn/payment.asp'
EWAY_PAYMENT_HOSTED_REAL_TIME_CVN_TESTING_MODE = 'https://www.eway.com.au/gateway_cvn/payment.asp'
EWAY_PAYMENT_STORED_LIVE = 'https://www.eway.com.au/gateway/xmlstored.asp'
EWAY_PAYMENT_MANAGED_TESTING_MODE = 'https://www.eway.com.au/gateway/ManagedPaymentService/test/managedCreditCardPayment.asmx'

EWAY_PAYMENT_LIVE_AUTH = 'https://www.eway.com.au/gateway/xmlauth.asp'
EWAY_PAYMENT_LIVE_AUTH_TESTING_MODE = 'https://www.eway.com.au/gateway/xmltest/authtestpage.asp'
EWAY_PAYMENT_LIVE_AUTH_CVN = 'https://www.eway.com.au/gateway_cvn/xmlauth.asp'
EWAY_PAYMENT_LIVE_AUTH_CVN_TESTING_MODE = 'https://www.eway.com.au/gateway_cvn/xmltest/authtestpage.asp'

EWAY_PAYMENT_LIVE_AUTH_COMPLETE = 'https://www.eway.com.au/gateway/xmlauthcomplete.asp'
EWAY_PAYMENT_LIVE_AUTH_COMPLETE_TESTING_MODE = 'https://www.eway.com.au/gateway/xmltest/authcompletetestpage.asp'

EWAY_PAYMENT_LIVE_AUTH_VOID = 'https://www.eway.com.au/gateway/xmlauthvoid.asp'
EWAY_PAYMENT_LIVE_AUTH_VOID_TESTING_MODE = 'https://www.eway.com.au/gateway/xmltest/authvoidtestpage.asp'

CUSTOMER_ID = "87654321"    # Set this to your eWAY Customer ID
PAYMENT_METHOD = REAL_TIME  # Set this to the payment gatway you would like to use (REAL_TIME, REAL_TIME_CVN or GEO_IP_ANTI_FRAUD)
USE_LIVE = False # Set this to true to use the live gateway


# define default values for eway
EWAY_DEFAULT_CUSTOMER_ID = 87654321
EWAY_DEFAULT_PAYMENT_METHOD = REAL_TIME # possible values are: REAL_TIME, REAL_TIME_CVN, GEO_IP_ANTI_FRAUD
EWAY_DEFAULT_LIVE_GATEWAY = False # <false> sets to testing mode, <true> to live mode