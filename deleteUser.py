import pingid
import sys

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'userName': sys.argv[1],
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/deleteuser/do', req_body)
