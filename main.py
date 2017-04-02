#!/usr/bin/python

import argparse
from reqs import *

def order_dish(rest, category, dish):
    login = LoginRequest()
    login.make()

    menu = MenuRequest(rest, DeliveryMethod.PICKUP)
    menu.make()

    addDish = AddDishRequest(rest, category, dish)
    addDish.make()

    confirmOrder = ConfirmOrderRequest()
    confirmOrder.make()

    payments = GetPaymentRequest()
    payments.make()

    if payments.payments is None:
        print "Failed to get payments :("
        exit()

    print "not submitting, remove this line to make this work"
    exit()

    submit = SubmitOrderRequest(rest, payments.payments)
    submit.make()
    submit.pprint_result()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Order food with 10bis')

    parser.add_argument('--rest', dest='rest', help="Restaurant")
    parser.add_argument('--cat', dest='category', help="Category")
    parser.add_argument('--dish', dest='dish', help="Dish")

    args = parser.parse_args()
    
    if args.rest is not None and args.category is not None and args.dish is not None:
        order_dish(args.rest, args.category, args.dish)