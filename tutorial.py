#Python 2.7.6
#tutorial.py

import requests
import json
import sys
from requests.auth import HTTPDigestAuth

# Format JSON output
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

base_url = 'https://tcnj.instructure.com' # Base URL with API
url = base_url + '/api/v1' # Path to Canvas API
# Use raw_input() to get data on a per user basis at runtime
userid = raw_input('User ID: ')
token = raw_input('Access Token: ')

myResponse = requests.get(url + '/users/' + '%s' %(userid) + '/courses/',headers = {'Authorization': 'Bearer ' + '%s' %(token)})
# print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):
    with open('courses.json', 'w') as outfile:
        json.dump(myResponse.content, outfile)

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)

    print("The response contains {0} properties".format(len(jData)))
    dump(jData)
else:
    # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()
