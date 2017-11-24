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

# Updates: daniela
@when(u'I do a "{method}" request with parameters to pivotal endpoint "{endpoint}"')
def step_impl(context, method, endpoint):
    if (context.first_module == "project"):
        if (context.second_module == "stories"):
            url = context.host + context.root_path + "/projects/{}/stories".format(context.proyect_id)
            context.result = context.r.do_request(method, url)
        elif (context.second_module == "story"):
            url = context.host + context.root_path + "/projects/{}/stories/{}".format(context.proyect_id, context.story_id)
            context.result = context.r.do_request(method, url)
        elif (context.second_module == "bulk"):
            url = context.host + context.root_path + "/projects/{}/stories/bulk".format(context.proyect_id)
            context.result = context.r.do_request(method, url)
        elif (context.second_module == "owners"):
            url = context.host + context.root_path + "/projects/{}/stories/{}/owner".format(context.proyect_id, context.story_id)
            context.result = context.r.do_request(method, url)
        elif (context.second_module == "task"):
            url = context.host + context.root_path + "/projects/{}/stories/{}/tasks/{}".format(context.proyect_id, context.story_id, context.task_id)
            context.result = context.r.do_request(method, url)
        elif (context.second_module == "tareas"):
            url = context.host + context.root_path + "/projects/{}/stories/{}/tasks".format(context.proyect_id, context.story_id)
            context.result = context.r.do_request(method, url)
        elif (context.second_module == "workspaces"):
            url = context.host + context.root_path + "/projects/{}/stories/{}/tasks".format(context.proyect_id, context.story_id)
            context.result = context.r.do_request(method, url)

# Autor: Ninoshka The user has an existent test "project" with existent(s) "bulk"
@given(u'The user has an existent test "{first_module}" with existent(s) "{second_module}"')
def step_impl(context, first_module, second_module):
    context.first_module=first_module
    context.second_module=second_module