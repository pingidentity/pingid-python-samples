import sys
import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'userName': 'asaf',
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/getactivationcode/do', req_body)
