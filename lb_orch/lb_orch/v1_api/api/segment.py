# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .api_data import SegmentData

api_segment = SegmentData()

class Segment(Resource):

    def get(self):
        print(g.headers)
        print(g.args)

        return api_segment.get_all_segments(), 200, None