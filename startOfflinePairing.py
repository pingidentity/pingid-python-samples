import sys
import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'username': 'asaf',
   'type':'EMAIL',
   'pairingData':'asaf@pingidentity.com',
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=False)
response_body = pingid.call('rest/4/startofflinepairing/do', req_body)
print(response_body)
