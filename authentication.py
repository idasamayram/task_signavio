import requests
from conf import *


def authenticate():
    login_url = base_url + '/p/login'   #POST/p/login: Requests Headers and forms the data parameters

    data = {'name': username,'password': password,'tokenonly': 'true'}  #gets the data from conf
    #if the user is in multiple workspaces, this additional data is also being handed out to server:
    if 'workspace_ID' in locals():  
        data['tenant'] = workspace_ID
    # authenticate using post
    login_request = requests.post(login_url, data)   
    # retrieve token and session ID
    auth_token = login_request.content.decode('utf-8')  #Decodes access token in utf-8 format
    jsesssion_ID = login_request.cookies['JSESSIONID']  #Cookie values for session ID 

    # The cookie is named 'LBROUTEID' for base_url 'editor.signavio.com' (which we need here),
    # 'AWSELB' for base_url 'app-au.signavio.com' and 'app-us.signavio.com'
    
    lb_route_ID = login_request.cookies['LBROUTEID']   #cookie values to route the request to the server that authenticated the request

    # return credentials
    return {'jsesssion_ID': jsesssion_ID, 'lb_route_ID': lb_route_ID, 'auth_token': auth_token}


authenticate()
