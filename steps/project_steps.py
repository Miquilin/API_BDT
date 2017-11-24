from behave import given, when, then
from utils import project_utils


@then(u'I receive a {service} list')
def step_impl(context, service):
    list_data = project_utils.getting_list(context, service)
    print('\tList of ', service, '(s) retrieved : ', len(list_data))


@then(u'I receive a {service} dictionary')
def step_impl(context, service):
    dict_data = project_utils.getting_dict(context, service)
    print('\tDictionary of ', service, '(s) retrieved : ', len(dict_data))


@then(u'I receive a {service} as result')
def step_impl(context, service):
    gral_data = project_utils.getting_object(context, service)


# Author: Rosario
@given(u'I have "{key}" with value "{value}"')
def step_impl(context, key, value):
    context.body[key] = value
    # print ("BODY :::::::::::: ", dict(context.body))


@then(u'I receive new object created')
def step_impl(context):
    print('\n RESULT: \n', context.result.text)
