import requests

class PivotalClient:


    def __init__(self):
        self.headers = {}
        self.endpoint = ''
        self.parameter = ''


    def do_request(self, method, endpoint, body=None):
        if method == 'GET':
            result = requests.get(endpoint, headers=self.headers)
        elif method == 'POST':
            result = requests.post(endpoint, headers=self.headers, data=body)
        return result



    def add_header(self, name, value):
        self.headers[name] = value


