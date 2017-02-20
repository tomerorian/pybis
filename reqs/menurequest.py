#!/usr/bin/python

from basicrequest import BasicRequest
import config

class DeliveryMethod:
    DELIVERY = "Delivery"
    PICKUP = "Pickup"

class MenuRequest(BasicRequest):
    def __init__(self, rest_id, delivery_method):
        self.rest_id = rest_id
        self.delivery_method = delivery_method

    def make(self):
        self.get("GetMenu", {"ResId": self.rest_id,
                             "deliveryMethod": self.delivery_method,
                             "encryptedUserId": None,
                             "shoppingCartGuid": None})

    def _on_success(self):
        pass