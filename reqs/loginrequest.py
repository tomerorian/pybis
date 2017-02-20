#!/usr/bin/python

from basicrequest import BasicRequest
import config

class LoginRequest(BasicRequest):

    def make(self):
        self.get("Login", {"UserName": None, "password": None})

    def _on_success(self):
        config.encrypteduserid = self.result["UserData"]["EncryptedUserId"]
        config.shoppingcartguid = self.result["ShoppingCartGuid"]
        print "Logged in"
        print "Encrypted user id set"
        print "Shopping cart id set to {cart_id}".format(cart_id=config.shoppingcartguid)