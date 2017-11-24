import requests

class PivotalClient:


    def __init__(self):
        self.headers = {}
        self.endpoint = ''
        self.parameter = {}


    def do_request(self, method, endpoint, body):
        if method == 'GET':
            result = requests.get(endpoint, headers=self.headers)
        elif method == 'POST':
            result = requests.post(endpoint, headers=self.headers, data=body)
        elif method == 'PUT':
            result = requests.put(endpoint, headers=self.headers, data=body)
        elif method == 'DELETE':
            result = requests.delete(endpoint, headers=self.headers)
        return result



    def add_header(self, name, value):
        self.headers[name] = value

    def add_parameter(self, name, value):
        self.parameter[name] = value

    def get_parameter(self):
        return self.parameter
