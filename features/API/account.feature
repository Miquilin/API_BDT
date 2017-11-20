Feature: account
  Access the account specified by the account_id value in the URL.

@smoke
Scenario:
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/accounts/1029778"
  Then I receive status code 200






