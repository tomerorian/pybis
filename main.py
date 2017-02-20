#!/usr/bin/python

from reqs import *

login = LoginRequest()
login.make()

menu = MenuRequest(8479, DeliveryMethod.PICKUP)
menu.make()

addDish = AddDishRequest(8479, 82430, 552761)
addDish.make()

payments = GetPaymentRequest()
payments.make()

if payments.payments is None:
    print "Failed to get payments :("
    exit()

exit()

submit = SubmitOrderRequest(8479, payments.payments)
submit.make()
submit.pprint_result()