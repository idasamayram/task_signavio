from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from conf import *
from authentication import authenticate

login_url = base_url + '/p/login'              #GET/p/login:Requests Headers and JSON parameters(authhandovertoken and redirect) 
                                               #and Responses the Set-Cookie for identifier, login,token, and session_ID, as well as token_ID and status codes

handover_url = base_url + '/p/authhandover'    #POST/p/authhandover:Requests headers and forms the response


redirect = '/p/explorer'                       #Redirects client to the Process Manager’s Explorer application

#reretrieving cookie values and headers from authenticate function
def retrieve_auth_token():
    auth_data = authenticate()                     
    # set credentials, response format
    cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
    headers = {'x-signavio-id': auth_data['auth_token']}
    
    #Requests headers and forms the response's cookie values
    handover_request = requests.post(handover_url,   
    cookies=cookies,
    headers=headers)
    
    #decodes the header and cookie responses into utf-8 format
    handover_token = handover_request.content.decode('utf-8')

    return handover_token

#performs GET to request the responses and headers and and redirect the responses as content-type to the client
class AuthenticationHandoverServer(BaseHTTPRequestHandler):
    def do_GET(self):
        redirect_url = '{0} ?authhandovertoken={1} &redirect={2} '.format(login_url, retrieve_auth_token(),redirect)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write( # return HTML redirect
            bytes('<meta http-equiv="refresh" content="0; url={0} " />'.format(redirect_url), 'utf-8'))

#starts an HTTP server on localhost:8081
def run():
    server_address = ('', 8081)
    server = HTTPServer(server_address, AuthenticationHandoverServer)
    print('Running authentication handover server on port 8081...')
    server.serve_forever()

run()
