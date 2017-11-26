import sys
import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'spAlias': 'web',
   'userName': 'asaf',
   'sessionId':'...', // required
    'otp':'...', // required
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/authoffline/do', req_body)
