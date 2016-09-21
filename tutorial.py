#Python 2.7.6
#RestfulClient.py

import requests
from requests.auth import HTTPDigestAuth
import json
import sys

def dump(obj, nested_level=0, output=sys.stdout):
    spacing = '   '
    if type(obj) == dict:
        print >> output, '%s{' % ((nested_level) * spacing)
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print >> output, '%s%s:' % ((nested_level + 1) * spacing, k)
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s: %s' % ((nested_level + 1) * spacing, k, v)
        print >> output, '%s}' % (nested_level * spacing)
    elif type(obj) == list:
        print >> output, '%s[' % ((nested_level) * spacing)
        for v in obj:
            if hasattr(v, '__iter__'):
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s' % ((nested_level + 1) * spacing, v)
        print >> output, '%s]' % ((nested_level) * spacing)
    else:
        print >> output, '%s%s' % (nested_level * spacing, obj)

# Replace with the correct URL
base_url = 'https://tcnj.instructure.com' # Base URL with API
url = base_url + '/api/v1'
account_id = '88968'
token = '19~zsbPmi9Fdj7rJ7ilOXVEtFdpavFRPUzt3EMA1TlWhQbsCbKVH6aQcQTSkHFS2qHK'
userid = '/5225612/'
# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
myResponse = requests.get(url + '/users/' +  userid + 'courses',headers = {'Authorization': 'Bearer ' + '%s' % token})
#print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    dump(jData)	
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()