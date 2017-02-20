#!/usr/bin/python

from basicrequest import BasicRequest

class GetPaymentRequest(BasicRequest):

    def __init__(self):
        self.payments = None

    def make(self):
        self.get("GetPaymentList", {"shoppingCartGuid": None})

    def _on_success(self):
        self.payments = self.result["Data"]