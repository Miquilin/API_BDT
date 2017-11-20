from compare import expect
from utils import pivot_client
# Autor: Miguel
@given(u'A valid {user} user token added on header')
def step_impl(context, user):
    context.r = pivot_client.PivotalClient()
    if user == "admin":
        context.r.add_header("X-TrackerToken", context.admin_token)
    elif user == "user":
        context.r.add_header("X-TrackerToken", context.user_token)
    else:
        print("user does not exist")

# Autor: Miguel
@when(u'I do a "{method}" request to pivotal endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    url = context.host + context.root_path + endpoint
    context.result = context.r.do_request(method, url)

# Autor: Miguel
@then(u'I receive status code {code}')
def step_impl(context, code):
    expect(str(context.result.status_code)).to_equal(code)

# Autor: Ninoshka
@given(u'The user has an existent test "{first_module}" with existent(s) "{second_module}"')
def step_impl(context, first_module, second_module):
    context.first_module=first_module
    context.second_module=second_module

# Autor: Ninoshka
@when(u'I do a "{method}" request with parameters to pivotal endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    if (context.first_module == "project"):
        if (context.second_module == "epic"):
            url = context.host + context.root_path + "/projects/{}/epics/{}".format(context.proyect_id,context.epic_id)
            context.result = context.r.do_request(method, url)
        elif (context.second_module == "epics"):
            url = context.host + context.root_path + "/projects/{}/epics".format(context.proyect_id)
            context.result = context.r.do_request(method, url)
        elif(context.second_module == "iterations"):
            url = context.host + context.root_path + "/projects/{}/iterations".format(context.proyect_id)
            context.result = context.r.do_request(method, url)
        elif(context.second_module == "labels"):
            url = context.host + context.root_path + "/projects/{}/labels".format(context.proyect_id)
            context.result = context.r.do_request(method, url)


