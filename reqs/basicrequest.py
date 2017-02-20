#!/usr/bin/python

import requests
import config
from os.path import join
import json

BASE_URL = "https://www.10bis.co.il/api"

class BasicRequest:
    def get(self, page, params):
        filled_params = self._fill_params(params)
        self._handle_response(requests.get(join(BASE_URL, page), params=filled_params))

    def post(self, page, json):
        json = self._fill_params(json)
        self._handle_response(requests.post(join(BASE_URL, page), json=json))

    def _fill_params(self, params):
        for param in params:
            if params[param] is None:
                params[param] = config.__dict__[param.lower()]

        return params

    def _handle_response(self, response):
        if response.status_code == 200:
            self.result = response.json()
            self._on_success()
        else:
            self.result = None

    def pprint_result(self):
        if self.result is not None:
            print json.dumps(self.result, indent=4, sort_keys=True)
        else:
            print self.result

    def _on_success(self):
        pass