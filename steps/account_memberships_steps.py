from compare import expect
from utils import Account_Membership
import json

@when(u'I do a "{method}" request with an account ID to pivotal endpoint "{endpoint}<account_id>/memberships"')
def step_impl(context, method, endpoint):
    url = context.host + context.root_path + endpoint + str(Account_Membership.AccountMembership.account_id) + "/memberships"
    context.result = context.r.do_request(method, url)


@then(u'membership {parameter} contains the right value')
def step_impl(context, parameter):
    print(context.result.text)
    data = json.loads(context.result.text)
    param = []
    if parameter == "kind":
        expect(data[parameter]).to_equal(Account_Membership.AccountMembership.kind)
    elif parameter == "id":
        expect(data[parameter]).to_equal(Account_Membership.AccountMembership.id)
    elif parameter == "person-kind":
        param = parameter.split('-')
        print(data[param[0][param[1]]])
        expect(data[param[0]][param[1]]).to_equal(Account_Membership.AccountMembership.person['kind'])
    elif parameter == "person-id":
        param = parameter.split('-')
        print(data[param[0][param[1]]])
        expect(data[param[0]][param[1]]).to_equal(Account_Membership.AccountMembership.person['id'])
    elif parameter == "person-name":
        param = parameter.split('-')
        print(data[param[0][param[1]]])
        expect(data[param[0]][param[1]]).to_equal(Account_Membership.AccountMembership.person['name'])
    elif parameter == "person-email":
        param = parameter.split('-')
        print(data[param[0][param[1]]])
        expect(data[parm[0]][param[1]]).to_equal(Account_Membership.AccountMembership.person['email'])
    elif parameter == "person-initials":
        param = parameter.split('-')
        print(data[param[0][param[1]]])
        expect(data[parm[0]][param[1]]).to_equal(Account_Membership.AccountMembership.person['initials'])
    elif parameter == "person-username":
        param = parameter.split('-')
        print(data[param[0][param[1]]])
        expect(data[param[0]][param[1]]).to_equal(Account_Membership.AccountMembership.person['username'])
    elif parameter == "account_id":
        expect(data[parameter]).to_equal(Account_Membership.AccountMembership.account_id)
    elif parameter == "owner":
        expect(data[parameter]).to_equal(Account_Membership.AccountMembership.owner)
    elif parameter == "admin":
        expect(data[parameter]).to_equal(Account_Membership.AccountMembership.admin)
    elif parameter == "project_creator":
        expect(data[0]).to_equal(Account_Membership.AccountMembership.project_creator)
    elif parameter == "timekeeper":
        expect(data[param]).to_equal(Account_Membership.AccountMembership.timekeeper)
    elif parameter == "time_enterer":
        expect(data[param]).to_equal(Account_Membership.AccountMembership.time_enterer)

