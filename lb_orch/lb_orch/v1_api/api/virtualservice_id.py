# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .api_data import VirtualServiceData

v_service_data = VirtualServiceData()


class VirtualserviceId(Resource):

    def get(self, id):
        print(g.args)

        return v_service_data.get_specific_virtual_service(), 200, None

    def put(self, id):
        print(g.json)

        return {'Error': 'something'}, 400, None

    def delete(self, id):

        return {'Error': 'something'}, 400, None