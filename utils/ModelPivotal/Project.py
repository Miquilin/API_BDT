from utils.ModelPivotal.Response import *
from utils.ModelPivotal.Epic import *
class Project:
    def __init__(self):
        self.id = 0
        self.name = "None"
        self.kind = "project"
        self.response = Response(0,"")
        self.epic_list=[]

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id=id

    def set_name(self, name):
        self.name = name

    def get_kind(self):
        return self.kind

    def set_kind(self, kind):
        self.kind = kind

    def get_response(self):
        return self.response

    def set_response(self, response):
        self.response = response

    def set_response_data(self, status_code, content):
        self.response.set_status_code(status_code)
        self.response.set_content(content)

    def get_epic_list(self):
        return self.epic_list

    def add_epic_list(self, epic):
        self.epic_list.append(epic)
