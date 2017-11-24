from compare import expect
from utils import json_utility
import json

@when(u'I do a "{method}" request with an account ID to pivotal endpoint "{endpoint}<account_id>"')
def step_impl(context, method, endpoint):
    context.js_util = json_utility.JsonUtility()
    context.account = context.js_util.read_json_from_file("account.json")
    id = context.js_util.search_item(context.account, "id")
    url = context.host + context.root_path + endpoint + str(id[0])
    context.result = context.r.do_request(method, url)

@then(u'Account {parameter} parameter contains the right value')
def step_impl(context, parameter):
    data = json.loads(context.result.text)
    if parameter == "kind":
        expect(context.js_util.search_item(data, "kind")).to_equal(context.js_util.search_item(context.account, "kind"))
    elif parameter == "id":
        expect(context.js_util.search_item(data, "id")).to_equal(context.js_util.search_item(context.account, "id"))
    elif parameter == "name":
        expect(context.js_util.search_item(data, "name")).to_equal(context.js_util.search_item(context.account, "name"))
    elif parameter == "status":
        expect(context.js_util.search_item(data, "status")).to_equal(context.js_util.search_item(context.account, "status"))
