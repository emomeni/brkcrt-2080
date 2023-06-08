import requests
import json
from pprint import pprint


# DevNet Sandbox Information
'''
Username: devnetmeraki@cisco.com
Password: Adm!n123!
You can also use this API key for the Dashboard API: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0
'''

MERAKI_API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# MERAKI BASE URL
base_url = "https://api.meraki.com/api/v1"
# requests header information
header = {"X-Cisco-Meraki-API-Key": MERAKI_API_KEY}


def get_org_list():
    endpoint = "/organizations"
    # Make request
    resp = requests.get(url=base_url+endpoint, headers=header)
    orgs = json.loads(resp.text)
    print(orgs)
    return orgs


def get_device_list():
    for org in orgs:
        # MERAKI Endpoint
        endpoint = "/organizations/{}/devices".format(org['id'])
        print(endpoint)
        resp = requests.get(url=base_url + endpoint, headers=header)
        device = json.loads(resp.text)
        pprint(device)


if __name__ == "__main__":
    orgs = get_org_list()
    get_device_list()