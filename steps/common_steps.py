from behave import given, when, then
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
    print('\t BODY : ', dict(context.body))
    context.result = context.r.do_request(method, url, context.body)


# Autor: Miguel
@then(u'I receive status code {code}')
def step_impl(context, code):
    # print ("I receive status code")
    expect(str(context.result.status_code)).to_equal(code)
