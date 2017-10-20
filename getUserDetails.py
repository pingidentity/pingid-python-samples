import pingid

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'getSameDeviceUsers':'false',
   'userName': 'asaf',
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/getuserdetails/do', req_body)
#print(response_body)
