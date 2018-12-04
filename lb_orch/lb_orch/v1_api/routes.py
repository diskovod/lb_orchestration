# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.sites_id import SitesId
from .api.virtualservice import Virtualservice
from .api.sites import Sites
from .api.segment import Segment
from .api.virtualservice_id import VirtualserviceId
from .api.segment_getNextSegment import SegmentGetnextsegment


routes = [
    dict(resource=SitesId, urls=['/sites/<id>'], endpoint='sites_id'),
    dict(resource=Virtualservice, urls=['/virtualservice'], endpoint='virtualservice'),
    dict(resource=Sites, urls=['/sites'], endpoint='sites'),
    dict(resource=Segment, urls=['/segment'], endpoint='segment'),
    dict(resource=VirtualserviceId, urls=['/virtualservice/<id>'], endpoint='virtualservice_id'),
    dict(resource=SegmentGetnextsegment, urls=['/segment/getNextSegment'], endpoint='segment_getNextSegment'),
]