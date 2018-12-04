# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from . api_data import SiteData

api_site = SiteData()

class Sites(Resource):

    def get(self):
        print(g.headers)

        return api_site.get_all_sites(), 200, None

    def post(self):
        print(g.json)
        print(g.headers)

        return [g.json], 201, None