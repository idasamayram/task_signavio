from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
from conf import *
from authentication import authenticate

login_url = base_url + '/p/login'
handover_url = base_url + '/p/authhandover'
redirect = '/p/explorer'


def retrieve_auth_token():
    auth_data = authenticate()
    # set credentials, response format
    cookies = {'JSESSIONID': auth_data['jsesssion_ID'], 'LBROUTEID': auth_data['lb_route_ID']}
    headers = {'x-signavio-id': auth_data['auth_token']}

    handover_request = requests.post(handover_url,
    cookies=cookies,
    headers=headers)

    handover_token = handover_request.content.decode('utf-8')

    return handover_token


class AuthenticationHandoverServer(BaseHTTPRequestHandler):
    def do_GET(self):
        redirect_url = '{0} ?authhandovertoken={1} &redirect={2} '.format(login_url, retrieve_auth_token(),redirect)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write( # return HTML redirect
            bytes('<meta http-equiv="refresh" content="0; url={0} " />'.format(redirect_url), 'utf-8'))


def run():
    server_address = ('', 8081)
    server = HTTPServer(server_address, AuthenticationHandoverServer)
    print('Running authentication handover server on port 8081...')
    server.serve_forever()

run()