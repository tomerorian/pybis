#!/usr/bin/python

from basicrequest import BasicRequest
import config

import logging
logger = logging.getLogger("pybis")

class LoginRequest(BasicRequest):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def make(self):
        self.get("Login", {"UserName": self.username, "password": self.password})

    def _on_success(self):
        config.encrypteduserid = self.result["UserData"]["EncryptedUserId"]
        config.shoppingcartguid = self.result["ShoppingCartGuid"]
        logger.info("Logged in")
        logger.info("Encrypted user id set")
        logger.info("Shopping cart id set to {cart_id}".format(cart_id=config.shoppingcartguid))