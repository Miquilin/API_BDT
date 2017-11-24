from utils.ModelPivotal import Project, Epic
from compare import expect

# Update: Ninoshka
@given(u'There is an existent "{service}"')
def step_impl(context, service):
    if(service == "epic"):
        expect(context.epic_test.get_id()).to_be_greater_than(0)


# Update: Ninoshka  And I need to "create" the "epic" with following <name>
@given(u'I need to "{method}" the "{service}" with following {name_test}')
def step_impl(context, method, service, name_test):
    if(method == "update"):
        context.name_updated = name_test
        context.r.add_parameter("name", context.name_updated)
    elif(method == "create"):
        context.r.add_parameter("name", name_test)

# Update: Ninoshka
@when(u'I do a "{method}" request with "{service}" method to pivotal endpoint "{endpoint}"')
def step_impl(context, method,service, endpoint):
    context.method =method
    if(str(endpoint).__contains__("epic_id")):
        context.url_test_scenario= context.url_test+"/"+service+"/{}".format(context.epic_id)
        context.result = context.r.do_request(method, context.url_test_scenario)
    else:
        context.url_test_scenario = context.url_test+ "/"+ service
        context.result = context.r.do_request(method, context.url_test_scenario)


# Autor: Ninoshka
@then(u'Response has "{parameter}" parameter with right value')
def step_impl(context, parameter):
    if (context.method == "PUT"):
        if (str(context.url_test_scenario).__contains__("epics")):
            epic_response_test = Epic.Epic()
            epic_response_test =context.tool_project.get_compare_object(context, "epics")
            if (parameter == "id"):
                expect(epic_response_test.get_id()).to_equal(context.epic_test.get_id())
            elif(parameter == "name"):
                expect(epic_response_test.get_name()).to_equal(context.epic_test.get_name())
            elif (parameter == "kind"):
                expect(epic_response_test.get_kind()).to_equal(context.epic_test.get_kind())
    elif(context.method == "POST"):
        if (str(context.url_test_scenario).__contains__("epics")):
            epic_response_test = Epic.Epic()
            epic_response_test =context.tool_project.get_compare_object(context, "epics")
            if (parameter == "name"):
                expect(epic_response_test.get_name()).to_equal(context.r.get_value_parameter(parameter))
            elif (parameter == "kind"):
                expect(epic_response_test.get_kind()).to_equal("epic")

@then(u'Response has new "{parameter}" parameter with right value')
def step_impl(context, parameter):
    if (str(context.url_test_scenario).__contains__("epics")):
        epic_response_test = Epic.Epic()
        epic_response_test =context.tool_project.get_compare_object(context, "epics")
        if(parameter == "name"):
            expect(epic_response_test.get_name()).to_equal(context.name_updated)




