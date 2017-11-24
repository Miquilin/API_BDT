import requests, json
from utils import pivot_client
from utils.ModelPivotal import Project, Epic
from utils.response_utils import get_an_object_response
import json
import yaml

class tool_project:
    global generic_data
    def __init__(self, user,host, root_path,admin_token , user_token ):
        #Inicial data as enviroment to python
        self.user_test = user
        self.host = host
        self.root_path = root_path
        self.admin_token = admin_token
        self.user_token = user_token
        #Inicial response
        self.response = pivot_client.PivotalClient()
        self.initial_response(self.user_test)

    def initial_response(self,user):
        if user == "admin":
            self.response.add_header("X-TrackerToken", self.admin_token)
        elif user == "user":
            self.response.add_header("X-TrackerToken", self.user_token)
        else:
            print("user does not exist")
#Project functionss
    def create_project_test(self, context, project_name_create):
        context.logger.info('Tool create_project_test')

        project_test= Project.Project()
        url = self.host + self.root_path + "/projects"
        self.response.add_parameter("name",project_name_create)
        project_test.set_name(project_name_create)
        self.result = self.response.do_request("POST", url,self.response.get_parameter() )
        context.logger.debug('Response is: {}'.format(self.result.text))
        project_test.set_response_data(self.result.status_code, self.result)
        print(self.result)
        data = json.loads(self.result.text)
        project_test = get_an_object_response(context,data, project_test)
        return project_test

    def get_all_project(self, context):
        project_test_list = []
        url = self.host + self.root_path + "/projects"
        self.result = self.response.do_request("GET", url)
        project_response_list = json.loads(self.result.text)
        for project_response in project_response_list:
            project_test = Project.Project()
            project_test_list.append(get_an_object_response(context, project_response, project_test))
        return project_test_list


    def get_a_project_by_name(self, context,name):
        context.logger.info('Tool get_a_project_by_name')
        response_project_list = self.get_all_project(context)
        for value in response_project_list:
            if(value.get_name() == name):
                return value
            else:
                context.logger.debug("get_a_project_by_name: {} does not exist".format(name))

    def delete_project_create_by_name( self,context, name):
        context.logger.info('Tool get_a_project_by_name')
        project_selected = self.get_a_project_by_name(context,name)
        if (project_selected != None):
            id=project_selected.get_id()
            if id!=0:
                url = self.host + self.root_path + "/projects/{}".format(id)
                self.result = self.response.do_request("DELETE", url)
                project_selected.set_response_data(self.result.status_code, self.result)
            else:
                print("delete_project_create_by_name: {} does not exist".format(name))

#Epic functionss /projects/{project_id}/epics/{epic_id}
    def create_epic_test(self, context, epic_name_create, project_id):
        epic_test=Epic.Epic()
        url = self.host + self.root_path + "/projects/{}/epics".format(project_id)
        self.response.add_parameter("name",epic_name_create)
        self.result = self.response.do_request("POST", url,self.response.get_parameter() )
        epic_test.set_response_data(self.result.status_code, self.result)
        data = json.loads(self.result.text)
        epic_test = get_an_object_response(context,data, epic_test)
        return epic_test

    def get_compare_object(self,context, service ):
        if (service == "epics"):
            epic_test = Epic.Epic()
            data = json.loads(context.result.text)
            epic_test = get_an_object_response(context, data, epic_test)
            return epic_test
