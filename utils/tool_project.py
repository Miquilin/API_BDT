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
        self.result = self.response.do_request("POST", url,self.response.get_parameter() )
        return self.result

    def get_all_project(self):
        url = self.host + self.root_path + "/projects"
        self.response.add_parameter("name", self.project_name_create)
        self.result = self.response.do_request("GET", url)
        print(self.result.text)
        return self.result


    def get_a_project_by_name(self, name):
        response_list = self.get_all_project()
        #for var in response_list:
        #    for vars_dictionary in var:
        #        print(vars_dictionary)
        #        if(vars_dictionary['name'] == name):
        #            id_project = vars_dictionary['id'].value()
        #            #url = self.host + self.root_path + "/project/{}".format(int(id_project))
        #            # id project
        #            url = self.host + self.root_path + "/project/{}".format(int(2123257))
        #            self.result = self.response.do_request("GET", url)
        #            print(self.result.text)
        #            return self.result


        # url = self.host + self.root_path + "/project/{}".format(int(id_project))
        # id project to delete: 2129903, "name":"new project"
        url = self.host + self.root_path + "/projects/{}".format(2123257)
        self.result = self.response.do_request("GET", url)
        print("get a project",self.result.text)
        return self.result


    def delete_project_create_by_name(self, name):

        return None