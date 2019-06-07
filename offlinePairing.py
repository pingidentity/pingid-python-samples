import sys
import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'username': 'asaf',
   'type':'SMS',
    'pairingData':'972521234567',
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/offlinepairing/do', req_body)
#print(response_body)
