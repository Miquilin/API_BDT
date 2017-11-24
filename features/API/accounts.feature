Feature: accounts
  Get all the accounts of which a use is an owner or admin.

@smoke
Scenario:
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/accounts"
  Then I receive status code 200

@crud
Scenario: Verify that it is possible to get the details of an account
  Given A valid admin user token added on header
  When I do a "GET" request with an account ID to pivotal endpoint "/accounts/<account_id>"
  Then I receive status code 200
    And Account kind parameter contains the right value
    And Account id parameter contains the right value
    And Account name parameter contains the right value
    And Account status parameter contains the right value
