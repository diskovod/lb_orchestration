# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .api_data import VirtualServiceData

v_service_data = VirtualServiceData()

class Virtualservice(Resource):

    def get(self):
        print(g.headers)
        print(g.args)
        print(v_service_data.get_all_virtualservices())
        return v_service_data.get_all_virtualservices(), 200, None

    def post(self):
        print(g.json)
        print(g.headers)

        return {'Error': 'something'}, 400, None
