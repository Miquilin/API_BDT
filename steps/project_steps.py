from behave import given, when, then
from utils import project_utils


@then(u'I receive projects list')
def step_impl(context):
    print("===================================")
    project_utils.printing_response(context,"Projects")
    print("===================================")


# To create a new project
@given(u'I will create project "My New Project"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I will create project "My New Project"')

@when(u'I sending a "POST" request to pivotal endpoint "/projects"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I sending a "POST" request to pivotal endpoint "/projects"')

@then(u'I receive the project id')
def step_impl(context):
    print(str(context.result.response))

@given(u'I have the project 123456')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have the project 123456')

@given(u'I need to update the project name to Editing my project')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I need to update the project name to Editing my project')

@given(u'I need to update the project description to This my descrption')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I need to update the project description to This my descrption')
