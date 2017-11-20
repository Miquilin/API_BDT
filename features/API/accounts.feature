Feature: accounts
  Get all the accounts of which a use is an owner or admin.

@smoke
Scenario:
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/accounts"
  Then I receive status code 200






