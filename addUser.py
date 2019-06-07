#uses commandline arguments to accept the name of the user and the activation status.
#args[1]: argument 1 = activationStatus.
#args[2]: argument 2 = UserName.

import pingid
import sys

PROPERTIES_FILE = './pingid.properties'

req_body = {
   'activateUser':sys.argv[1],
   'role':'REGULAR',
   'userName': sys.argv[2],
  }

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)
response_body = pingid.call('rest/4/adduser/do', req_body)
