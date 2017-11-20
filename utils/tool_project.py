import requests, json
from utils import pivot_client
from utils.ModelPivotal import Project
import yaml

class tool_project:
    global generic_data
    def __init__(self, user, name_project_test):
        #Inicial data as enviroment to python
        generic_data = yaml.load(open('../settings/config.yml'))
        self.host = generic_data['app']['host']
        self.root_path = generic_data['app']['root_path']
        self.admin_token = generic_data['users']['admin_token']
        self.user_token = generic_data['users']['user_token']
        # ninoshka Existent_data_read
        self.proyect_id = generic_data['project_test_data']['proyect_id']
        self.epic_id = generic_data['project_test_data']['epic_id']
        self.project_name = generic_data['project_test_data']['project_name']
        # ninoshka New_data_create_edit
        self.project_name_create = generic_data['project_test_data_create']['project_name']
        #Inicial response
        self.response = pivot_client.PivotalClient()
        self.user_test = user
        if user == "admin":
            self.response.add_header("X-TrackerToken", self.admin_token)
            print("user is ", user)
        elif user == "user":
            self.response.add_header("X-TrackerToken", self.user_token)
        else:
            print("user does not exist")
        # Delete a project if exist it on database
        self.delete_project_create_by_name(name_project_test)

    def create_project_test(self):
        project_test= Project.Project()
        url = self.host + self.root_path + "/projects"
        self.response.add_parameter("name",self.project_name_create)
        print(self.response.get_parameter())
        print(url)
        self.result = self.response.do_request("POST", url,self.response.get_parameter() )
        print("self.result.status_code", self.result.status_code)
        return self.result.status_code

    def get_all_project(self):

        return None


    def get_a_project_by_name(self, name):
        return self

    def delete_project_create_by_name(self, name):
        return None