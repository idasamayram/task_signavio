import requests
from conf import *
from authentication.authenticate import authenticate

# user variables
# ID of the diagram revision you want to retrieve
revision_ID = '<revision_ID>'
format = 'json'  # data format: json, bpmn2_0_xml, PNG or SVG

diagram_url = base_url + '/p/revision'

auth_data = authenticate()

# set credentials, response format
cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
headers = {'Accept': 'application/json', 'x-signavio-id':  auth_data['auth_token']}

get_diagram_request = requests.get(diagram_url + '/' + revision_ID + '/' + format, cookies=cookies, headers=headers)

print(get_diagram_request.text)