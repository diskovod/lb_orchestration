# coding: utf-8

"""
    CESv2 Remail Network API

    CESv2 Remail Network API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: cie-eng.network-hps-team@cisco.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.site_api import SiteApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSiteApi(unittest.TestCase):
    """SiteApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.site_api.SiteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_site(self):
        """Test case for create_site

        Add new site definition  # noqa: E501
        """
        pass

    def test_get_all_sites(self):
        """Test case for get_all_sites

        Finds all supported sites  # noqa: E501
        """
        pass

    def test_get_site(self):
        """Test case for get_site

        Get site by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
