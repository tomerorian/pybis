#!/usr/bin/python

from basicrequest import BasicRequest
import config

import logging
logger = logging.getLogger("pybis")

class SubmitOrderRequest(BasicRequest):

    def __init__(self, rest_id, payments):
        self.rest_id = rest_id
        self.payments = payments

    def make(self):
        self.post("SubmitOrder", self._get_body())

    def _on_success(self):
        logger.info("Order is out!")

    def _get_body(self):
        return {
            "dontwantcultery": 0,
            "remarks": "",
            "resId": self.rest_id,
            "shoppingCartGuid": None,
            "encryptedUserId": None,
            "payments": self.payments
        }