from utils.ModelPivotal import Project, Epic
from compare import expect

# Autor: Ninoshka
@when(u'I do a "{method}" request with "{service}" method to pivotal endpoint "{endpoint}"')
def step_impl(context, method,service, endpoint):
    if(str(endpoint).__contains__("epic_id")):
        context.url_test_scenario= context.url_test+"/"+service+"/{}".format(context.epic_id)
        context.result = context.r.do_request(method, context.url_test_scenario)
    else:
        context.url_test_scenario = context.url_test+ "/"+ service
        context.result = context.r.do_request(method, context.url_test_scenario)

# Autor: Ninoshka
@then(u'Response has "{parameter}" parameter with right value')
def step_impl(context, parameter):
    if (str(context.url_test_scenario).__contains__("epics")):
        epic_response_test = Epic.Epic()
        epic_response_test =context.tool_project.get_compare_object(context, "epics")
        if (parameter == "id"):
            expect(epic_response_test.get_id()).to_equal(context.epic_test.get_id())
        elif(parameter == "name"):
            expect(epic_response_test.get_name()).to_equal(context.epic_test.get_name())
        elif (parameter == "kind"):
            expect(epic_response_test.get_kind()).to_equal(context.epic_test.get_kind())