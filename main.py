#!/usr/bin/python

import argparse
from reqs import *

def order_dish(rest, category, dish):
    # Logs in, gets and sets our user id and shopping cart id in the config
    login = LoginRequest()
    login.make()

    # Making the menu request sets the delivery method
    menu = MenuRequest(rest, DeliveryMethod.PICKUP)
    menu.make()

    # Adds the wanted dish to the shopping cart
    addDish = AddDishRequest(rest, category, dish)
    addDish.make()

    # Confirming the order is not a must, but it applies hourly coupons if present
    confirmOrder = ConfirmOrderRequest()
    confirmOrder.make()

    # Gets the payment split to make (needed for submitting the order)
    payments = GetPaymentRequest()
    payments.make()

    if payments.payments is None:
        print "Failed to get payments :("
        exit()

    print "not submitting, remove this line to make this work"
    exit()

    # The final call that actually makes the order
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