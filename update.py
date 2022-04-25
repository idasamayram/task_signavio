import codecs, requests
import json

from conf import *
from authentication.authenticate import authenticate

# user variables
diagram_ID = '<diagram_ID>'
parent_ID = '<parent_ID>'  # ID of the target directory

comment = 'new comment'

revision_url = base_url + '/p/model/' + diagram_ID + '/revisions'

auth_data = authenticate()

# set credentials, response format
cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
headers = {'Accept': 'application/json',
           'x-signavio-id':  auth_data['auth_token']}

get_revisions_request = requests.get(revision_url,
                                     cookies=cookies,
                                     headers=headers)




data_all = json.loads(get_revisions_request.text)[0]

name = data_all['name']
file_path = data_all['file_path']


model_url = base_url + '/p/model'

auth_data = authenticate()
# set credentials, response format
cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
headers = {'Accept': 'application/json',
           'x-signavio-id':  auth_data['auth_token']}




with codecs.open(file_path, 'r', 'utf-8') \
        as file_import_stream:
    json_data = file_import_stream.read()

data = {
   'name': name,
   'json_xml': json_data,
   'parent': parent_ID,
   'comment': comment
}
update_diagram_request = requests.put(model_url + '/' + diagram_ID,
                                       cookies=cookies,
                                       headers=headers,
                                       data=data)

result = str(update_diagram_request.content)

print('updating diagram: ' + result)