# get user details

import json
import base64
import arrow
import requests
from jose import jwt

locale = 'en'
get_user_details_endpoint = 'https://idpxnyl3m.pingidentity.com/pingid/rest/4/getuserdetails/do'

api_version = '4.9.17'

org_alias = 'ORG_ALIAS'
use_base64_key = base64.urlsafe_b64decode('BASE64_SECRET_KEY')
token = 'TOKEN'

user_name = 'USER_NAME'

get_user_details_req_headers = {
  'alg': 'HS256',
  'org_alias': org_alias,
  'token': token
}

get_user_details_req_payload = {
  'reqHeader': {
    'locale': locale,
    'orgAlias': org_alias,
    'secretKey': token,
    'timestamp': arrow.utcnow().format('YYYY-MM-DD HH:mm:ss.SSS'),
    'version': api_version
  },
 'reqBody': {
   'getSameDeviceUsers':'false',
   'userName': user_name,
  }
}

get_user_details_req_jwt = jwt.encode(get_user_details_req_payload, use_base64_key, algorithm='HS256', headers=get_user_details_req_headers)

print('{0}Request Payload{0}\n{1}\n'.format('='*20, get_user_details_req_jwt))

r = requests.post(url=get_user_details_endpoint, data=get_user_details_req_jwt, headers={'Content-Type':'application/json'})

print(r.status_code)

print('{0}Response Payload{0}\n{1}\n'.format('='*20, r.content))
extracted_response = jwt.decode(r.content, use_base64_key, algorithms=['HS256'])
json_response=json.dumps(extracted_response, indent=2)
print('{0}Response Extracted{0}\n{1}\n'.format('='*20, json_response))
