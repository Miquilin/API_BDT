from yaml import *
import datetime
import logging
from random import randint
from utils.tool_project import *

global generic_data

generic_data = yaml.load(open('settings/config.yml'))


def before_all(context):
    context.host = generic_data['app']['host']
    context.root_path = generic_data['app']['root_path']
    context.admin_token = generic_data['users']['admin_token']
    context.user_token = generic_data['users']['user_token']
    context.body = {}
    create_logger(context)

def before_scenario(context,scenario):
    if ("admin" in scenario.tags):
        context.user = "admin"
    else:
        context.user = "user"
    context.tool_project = tool_project(context.user,context.host, context.root_path, context.admin_token,
                                                     context.user_token)
    context.body = {}
    context.body.clear()

    if ("add_project_id" in scenario.tags):
        context.name_project= "Project{}".format(randint(1, 100))
        context.project_test= context.tool_project.create_project_test(context, context.name_project)
        context.project_id = context.project_test.get_id()
        context.logger.info('Tags is add_project_id')
        context.logger.debug('Tags is add_project_id: {}'.format(context.project_id))
        context.epic_id = 0
        context.url_test=context.host + context.root_path + "/projects/{}".format(context.project_id)
    if ("add_epic_id" in scenario.tags):
        context.logger.debug('Tags is add_epic_id: {}'.format(context.epic_id))
        context.epic_test = context.tool_project.create_epic_test(context,"epic_test_dont_touch",context.project_id )
        context.epic_id = context.epic_test.get_id()

def after_scenario(context,scenario):
    if ("add_project_id" in scenario.tags):
        context.project_test= context.tool_project.delete_project_create_by_name(context, context.name_project)


def create_logger(context):
    context.logging = logging.basicConfig(level=logging.DEBUG)
    context.logger = logging.getLogger(__name__)
    #Log names  with a current date
    context.handler = logging.FileHandler('Log_execution_test_{}.log'.format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S")))
    context.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    context.handler.setFormatter(context.formatter)
    context.logger.addHandler(context.handler)