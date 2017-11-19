Feature: Account Memberships
  List all of the memberships in an account.

@smoke
Scenario:
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/accounts/1029778/memberships"
  Then I receive status code 200






