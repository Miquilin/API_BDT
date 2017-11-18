import yaml

global generic_data
generic_data = yaml.load(open('../../settings/config.yml'))

def before_all(context):
    context.host = generic_data['app']['host']
    context.root_path = generic_data['app']['root_path']
    context.admin_token = generic_data['users']['admin_token']
    context.user_token = generic_data['users']['user_token']