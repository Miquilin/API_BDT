import requests

class PivotalClient:


    def __init__(self):
        self.headers = {}
        self.endpoint = ''
        self.parameter = {}


    def do_request(self, method, endpoint, body=None):
        result=None
        if method == 'GET':
            result = requests.get(endpoint, headers=self.headers)
        elif method == 'POST':
            if(len(self.parameter) !=0):
                result = requests.post(endpoint, headers=self.headers,data= self.parameter)
                print(result.text)
            else:
                result = requests.post(endpoint, headers=self.headers, data=body)
        elif method == 'DELETE':
            result = requests.delete(endpoint, headers=self.headers)
        elif method == 'PUT':
            if (len(self.parameter) != 0):
                result = requests.put(endpoint, headers=self.headers, data=self.parameter)
            else:
                result = requests.put(endpoint, headers=self.headers, data=body)
        return result




    def add_header(self, name, value):
        self.headers[name] = value

    def add_parameter(self, name, value):
        self.parameter[name] = value

    def get_parameter(self):
        return self.parameter

    def get_value_parameter(self, key_input):
        for key, value in self.parameter.items():
            if key == key_input:
                return value
