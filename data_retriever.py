import requests

from conf import *
from authentication import authenticate

# user variables
# ID of the diagram revision you want to retrieve the data
diagram_ID = '<diagram_ID>'

revision_url = base_url + '/p/model/' + diagram_ID + '/revisions'      #GET/p/model/(id)/revisions:Retrieves a diagram’s revisions, with each revision’s metadata.
                                                                       #Requests the id and the request headers, then responses the meta data of each id's revision.
format = 'json'                                                        # data format: json, bpmn2_0_xml, PNG or SVG           

auth_data = authenticate()                                             #reretrieving cookie values and headers from authenticate function

# set credentials, response format
cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
headers = {'Accept': 'application/json',
           'x-signavio-id':  auth_data['auth_token']}

#requests the revision id's meta data
get_revisions_request = requests.get(revision_url + '/' + format,
                                     cookies=cookies,
                                     headers=headers)

print(get_revisions_request.text)
