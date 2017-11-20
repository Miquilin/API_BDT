import yaml

global generic_data
generic_data = yaml.load(open('../../settings/config.yml'))

def before_all(context):
    context.host = generic_data['app']['host']
    context.root_path = generic_data['app']['root_path']
    context.admin_token = generic_data['users']['admin_token']
    context.user_token = generic_data['users']['user_token']
    #ninoshka Existent_data_read
    context.proyect_id = generic_data['project_test_data']['proyect_id']
    context.epic_id = generic_data['project_test_data']['epic_id']
    context.project_name = generic_data['project_test_data']['project_name']
    #ninoshka New_data_create_edit
    context.project_name_create = generic_data['project_test_data_create']['project_name']