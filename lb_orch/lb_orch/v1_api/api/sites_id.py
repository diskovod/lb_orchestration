# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .api_data import SiteData

api_site = SiteData()


class SitesId(Resource):

    def get(self, id):
        print(g.headers)

        if id == "0":
            site_data = [{
            "id": 0,
            "name": "sv2",
            "provider": "avi",
            "update_interval": 0
            }]
        else:
            site_data = []


        return site_data, 200, None