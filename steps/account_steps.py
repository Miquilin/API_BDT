from compare import expect
from utils import Account
import json

@when(u'I do a "{method}" request with an account ID to pivotal endpoint "{endpoint}<account_id>"')
def step_impl(context, method, endpoint):
    url = context.host + context.root_path + endpoint + str(Account.Account.id)
    context.result = context.r.do_request(method, url)

@then(u'Account {parameter} parameter contains the right value')
def step_impl(context, parameter):
    data = json.loads(context.result.text)
    if parameter == "kind":
        expect(data[parameter]).to_equal(Account.Account.kind)
    elif parameter == "id":
        expect(data[parameter]).to_equal(Account.Account.id)
    elif parameter == "name":
        expect(data[parameter]).to_equal(Account.Account.name)
    elif parameter == "status":
        expect(data[parameter]).to_equal(Account.Account.status)