#!/usr/bin/python

from basicrequest import BasicRequest
import config

class AddDishRequest(BasicRequest):

    def __init__(self, rest_id, category_id, dish_id):
        self.rest_id = rest_id
        self.category_id = category_id
        self.dish_id = dish_id

    def make(self):
        self.post("AddDish", self._get_body())

    def _on_success(self):
        print "Dish added successfully"

    def _get_body(self):
        return {
            "dishToSubmit": {
                "AssignedUserId": -1,
                "Choises": [],
                "DishNotes": "",
                "DishOwnerId": self.category_id,
                "ID": self.dish_id,
                "orderIndex": 0,
                "Quantity": 1
            },
            "encryptedUserId": None,
            "resId": self.rest_id,
            "shoppingCartGuid": None,
            "Domainid": "10bis",
            "Websiteid": "10bis"
        }