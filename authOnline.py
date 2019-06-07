import sys
import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'spAlias': 'web',
   'userName': 'asaf',
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/authonline/do', req_body)
