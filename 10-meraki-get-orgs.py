import requests
import json
from pprint import pprint
# DevNet Sandbox Information
from requests import Response
'''
Username: devnetmeraki@cisco.com
Password: Adm!n123!
You can also use this API key for the Dashboard API: 6bec40cf957de430a6f1f2baa056b99a4fac9ea0
'''
MERAKI_API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# MERAKI BASE URL
base_url = "https://api.meraki.com/api/v1"
# MERAKI Endpoint
endpoint = "/organizations"
# requests header information
header = {"X-Cisco-Meraki-API-Key": MERAKI_API_KEY}
# Make request
Response = requests.get(url=base_url+endpoint, headers=header)
# orgs = json.loads(orgs.text)
pprint(Response.json())


