import codecs, requests

from conf import *
from authentication import authenticate

# user variables (desired changes)
diagram_ID = '<diagram_ID>'
parent_ID = '<parent_ID>'  # ID of the target directory
name = 'Receipt of application (future state)'  # Name of the diagram
file_path = 'files/receipt_of_application.json'  # location of JSON data
comment = 'adjust to future state'

model_url = base_url + '/p/model'  #Retrieving the current meta data of the diagram

auth_data = authenticate()

# set credentials, response format
cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
headers = {'Accept': 'application/json',
           'x-signavio-id':  auth_data['auth_token']}

#reading the JSON representation of new revision as utf-8 format
with codecs.open(file_path, 'r', 'utf-8') \
        as file_import_stream:
    json_data = file_import_stream.read()

#updating the data according to user variable changes
data = {
   'name': name,
   'json_xml': json_data,
   'parent': parent_ID,
   'comment': comment
}
update_diagram_request = requests.put(model_url + '/' + diagram_ID,      #PUT/p/model/(id): Updates the specified diagram, by creating a new diagram revision.
                                       cookies=cookies,
                                       headers=headers,
                                       data=data)

#converting the updated data as string to print
result = str(update_diagram_request.content)

print('updating diagram: ' + result)