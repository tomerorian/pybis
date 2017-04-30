#!/usr/bin/python

from basicrequest import BasicRequest
import config

import logging
logger = logging.getLogger("pybis")

class ConfirmOrderRequest(BasicRequest):

    def __init__(self):
        pass

    def make(self):
        self.get("OrderConfirmation", self._get_body())

    def _on_success(self):
        logger.info("Order confirmed")

    def _get_body(self):
        return {
            "encryptedUserId": None,
            "shoppingCartGuid": None,
            "Domainid": "10bis",
            "Websiteid": "10bis"
        }