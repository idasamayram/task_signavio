import codecs, os, requests
from conf import *
from authentication import authenticate

# user variables
directory_ID = '<directory_ID>'  # ID of the target directory
# relative path to directory containing the BPMN XML files:
dir_name = 'files'

import_url = base_url + '/p/bpmn2_0-import'
 
auth_data = authenticate()        #retrieve data from authenticate function

# set credentials, response format
cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
headers = {'Accept': 'application/json', 'x-signavio-id':  auth_data['auth_token']}
#  import file
def import_file(filename, filepath):
    with codecs.open(filepath, 'r', 'utf-8') as file_import_stream:
        file_import_str = file_import_stream.read()
        import_request = requests.post(import_url, cookies=cookies, headers=headers, files={'bpmn2_0file': (filename, file_import_str)}, data={'directory': directory_ID, 'filename': filename})
        print(filepath + ': ' + str(import_request.content))


for name in os.listdir(dir_name):
    path = dir_name + '/' + name
    import_file(name, path)
