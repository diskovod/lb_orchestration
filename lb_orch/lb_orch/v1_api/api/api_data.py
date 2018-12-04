import json

class VirtualServiceData:
    def __init__(self):
        self.virtualservice = [{'server_pool':
                                   {'servers':
                                        [
                                            {'enabled': True,
                                             'ip': {'addr': '10.8.128.53',
                                                    'type': 'V4'}
                                             }
                                        ],
                                            'lb_algorithm': 'LB_ALGORITHM_LEAST_CONNECTIONS'
                                   },
                                'site_id': 2,
                                'nat':
                                    {'ip_address': {}},
                                'name': 'hc2516-81.iphmx.com',
                                'segment_id': 0,
                                'vip': {'ip_address': {}}
                                }]

        self.virtualservice_by_id = [{"id": "2-virtualservice-a1074738-d032-44de-b663-45928b3db451",
                                      "site_id": 2,
                                      "segment_id": 0,
                                      "name": "hc2516-81.iphmx.com",
                                      "vip":
                                          {
                                              "ip_address":
                                            {
                                              "type": "V4",
                                              "address": "68.232.129.60"
                                            }
                                          },
                                      "nat":
                                          {
                                                "ip_address":
                                                    {
                                                        "type": "V4",
                                                        "address": "68.232.129.60"
                                                    }
                                          },
                                      "server_pool": {
                                          "lb_algorithm": "LB_ALGORITHM_LEAST_CONNECTIONS",
                                          "servers": [
                                              {
                                                  "ip": {
                                                      "type": "V4",
                                                      "addr": "10.8.128.53"
                                                  },

                                                  "enabled": "true"
                                              }
                                          ]
                                      },
                                      "createdAt": "2018-04-05T01:02:14.000Z",
                                      "modifiedAt": "2018-04-05T01:03:18.000Z",
                                      "deploymentStatus": "deleted"
                                      }]


    def get_all_virtualservices(self):
        return self.virtualservice

    def get_specific_virtual_service(self):
        return self.virtualservice_by_id


class SiteData:
    def __init__(self):
        self.site = [{
            "id": 0,
            "name": "sv2",
            "provider": "avi",
            "update_interval": 0
        }]




    def get_all_sites(self):
        return self.site

class SegmentData:
    def __init__(self):
        self.segment = [
  {
    "id": 0,
    "site_id": "2",
    "max_vs": "250",
    "avail_vs": "200",
    "vlan": "301",
    "subnets": [
      {
        "type": "V4",
        "subnet_id": "10.10.0.0",
        "mask_bits": "24"
      }
    ]
  }
]

    def get_all_segments(self):
        return self.segment