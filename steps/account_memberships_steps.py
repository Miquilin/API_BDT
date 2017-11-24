from compare import expect
from utils import json_utility
import json

@when(u'I do a "{method}" request with an account ID to pivotal endpoint "{endpoint}<account_id>/memberships"')
def step_impl(context, method, endpoint):
    context.js_util = json_utility.JsonUtility()
    context.account_member = context.js_util.read_json_from_file("account.json")
    id = context.js_util.search_item(context.account_member, "id")
    url = context.host + context.root_path + endpoint + str(id[0]) + "/memberships"
    context.result = context.r.do_request(method, url)


@when(u'I do a "{method}" request with a person id {person_id} to pivotal endpoint "{endpoint}"')
def step_impl(context, method, person_id, endpoint):
    context.js_util = json_utility.JsonUtility()
    if method == "POST":
        context.membership = context.js_util.read_json_from_file("new_membership_resp.json")
        url = context.host + context.root_path + endpoint
        body = {"person_id": person_id}
        context.result = context.r.do_request(method, url, body)
    if method == "PUT":
        context.membership = context.js_util.read_json_from_file("update_membership_resp.json")
        url = context.host + context.root_path + endpoint
        body = {"timekeeper": "true"}
        context.result = context.r.do_request(method, url, body)
    if method == "DELETE":
        context.account_member = context.js_util.read_json_from_file("account.json")
        url = context.host + context.root_path + endpoint
        context.result = context.r.do_request(method, url)



@then(u'membership {parameter} contains the right value')
def step_impl(context, parameter):
    data = json.loads(context.result.text)
    if parameter == "kind":
        expect(context.js_util.search_item(data, "kind")).to_equal(context.js_util.search_item(context.account_member, "kind"))
    elif parameter == "id":
        expect(context.js_util.search_item(data, "id")).to_equal(context.js_util.search_item(context.account_member, "id"))
    elif parameter == "person-kind":
        expect(context.js_util.search_item(data, "kind")).to_equal(context.js_util.search_item(context.account_member, "kind"))
    elif parameter == "person-id":
        expect(context.js_util.search_item(data, "id")).to_equal(context.js_util.search_item(context.account_member, "id"))
    elif parameter == "person-name":
        expect(context.js_util.search_item(data, "name")).to_equal(context.js_util.search_item(context.account_member, "name"))
    elif parameter == "person-email":
        expect(context.js_util.search_item(data, "email")).to_equal(context.js_util.search_item(context.account_member, "email"))
    elif parameter == "person-initials":
        expect(context.js_util.search_item(data, "initials")).to_equal(context.js_util.search_item(context.account_member, "initials"))
    elif parameter == "person-username":
        expect(context.js_util.search_item(data, "username")).to_equal(context.js_util.search_item(context.account_member, "username"))
    elif parameter == "account_id":
        expect(context.js_util.search_item(data, "account_id")).to_equal(context.js_util.search_item(context.account_member, "account_id"))
    elif parameter == "owner":
        expect(context.js_util.search_item(data, "owner")).to_equal(context.js_util.search_item(context.account_member, "owner"))
    elif parameter == "admin":
        expect(context.js_util.search_item(data, "admin")).to_equal(context.js_util.search_item(context.account_member, "admin"))
    # elif parameter == "project_creator":
    #     expect(context.js_util.search_item(data, "project_creator")).to_equal(context.js_util.search_item(context.account_member, "project_creator"))
    # elif parameter == "timekeeper":
    #      expect(context.js_util.search_item(data, "timekeeper")).to_equal(context.js_util.search_item(context.account_member, "timekeeper"))
    # elif parameter == "time_enterer":
    #      expect(context.js_util.search_item(data, "time_enterer")).to_equal(context.js_util.search_item(context.account_member, "time_enterer"))


@then(u'new membership {parameter} contains the right value')
def step_impl(context, parameter):
    data = json.loads(context.result.text)
    if parameter == "kind":
        expect(context.js_util.search_item(data, "kind")).to_equal(context.js_util.search_item(context.membership, "kind"))
    elif parameter == "id":
        expect(context.js_util.search_item(data, "id")).to_equal(context.js_util.search_item(context.membership, "id"))
    elif parameter == "person-kind":
        expect(context.js_util.search_item(data, "kind")).to_equal(context.js_util.search_item(context.membership, "kind"))
    elif parameter == "person-id":
        expect(context.js_util.search_item(data, "id")).to_equal(context.js_util.search_item(context.membership, "id"))
    elif parameter == "person-name":
        expect(context.js_util.search_item(data, "name")).to_equal(context.js_util.search_item(context.membership, "name"))
    elif parameter == "person-email":
        expect(context.js_util.search_item(data, "email")).to_equal(context.js_util.search_item(context.membership, "email"))
    elif parameter == "person-initials":
        expect(context.js_util.search_item(data, "initials")).to_equal(context.js_util.search_item(context.membership, "initials"))
    elif parameter == "person-username":
        expect(context.js_util.search_item(data, "username")).to_equal(context.js_util.search_item(context.membership, "username"))
    elif parameter == "account_id":
        expect(context.js_util.search_item(data, "account_id")).to_equal(context.js_util.search_item(context.membership, "account_id"))
    elif parameter == "owner":
        expect(context.js_util.search_item(data, "owner")).to_equal(context.js_util.search_item(context.membership, "owner"))
    elif parameter == "admin":
        expect(context.js_util.search_item(data, "admin")).to_equal(context.js_util.search_item(context.membership, "admin"))
    # elif parameter == "project_creator":
    #     expect(context.js_util.search_item(data, "project_creator")).to_equal(context.js_util.search_item(context.membership, "project_creator"))
    # elif parameter == "timekeeper":
    #      expect(context.js_util.search_item(data, "timekeeper")).to_equal(context.js_util.search_item(context.membership, "timekeeper"))
    # elif parameter == "time_enterer":
         # expect(context.js_util.search_item(data, "time_enterer")).to_equal(context.js_util.search_item(context.membership, "time_enterer"))

@then(u'membership timekeeper parameter contains the {boolean} value')
def step_impl(context, boolean):
    data = json.loads(context.result.text)
    expect(str(context.js_util.search_item(data, "timekeeper"))).to_equal('[True]')
