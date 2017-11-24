Feature: Account Memberships
  List all of the memberships in an account.

@smoke
Scenario:
  Given A valid admin user token added on header
  When I do a "GET" request with an account ID to pivotal endpoint "/accounts/<account_id>/memberships"
  Then I receive status code 200


@crud
Scenario: Verify that it is possible to get the list of memberships of an account
  Given A valid admin user token added on header
  When I do a "GET" request with an account ID to pivotal endpoint "/accounts/<account_id>/memberships"
  Then I receive status code 200
    And membership kind parameter contains the right value
    And membership id parameter contains the right value
    And membership person-kind parameter contains the right value
    And membership person-id parameter contains the right value
    And membership person-name parameter contains the right value
    And membership person-email parameter contains the right value
    And membership person-initials parameter contains the right value
    And membership person-username parameter contains the right value
    And membership account_id parameter contains the right value
    And membership owner parameter contains the right value
    And membership admin parameter contains the right value
    And membership project_creator contains the right value
    And membership timekeeper contains the right value
    And membership time_enterer contains the right value

 @crud
Scenario Outline: Verify that the user is able to add an existent membership into the account
   Given A valid admin user token added on header
   When I do a "POST" request with a person id <person_id> to pivotal endpoint "/accounts/<account_id>/memberships"
   Then I receive status code 200
    And new membership kind parameter contains the right value
    And new membership id parameter contains the right value
    And new membership person-kind parameter contains the right value
    And new membership person-id parameter contains the right value
    And new membership person-name parameter contains the right value
    And new membership person-email parameter contains the right value
    And new membership person-initials parameter contains the right value
    And new membership person-username parameter contains the right value
    And new membership account_id parameter contains the right value
    And new membership owner parameter contains the right value
    And new membership admin parameter contains the right value
    And new membership project_creator contains the right value
    And new membership timekeeper contains the right value
    And new membership time_enterer contains the right value
Examples:
   |person_id |account_id |
   |3002807   |1033029    |


 @crud
Scenario Outline: Verify that the user is able to update an existent membership into the account
   Given A valid admin user token added on header
   When I do a "PUT" request with a person id <person_id> to pivotal endpoint "/accounts/<account_id>/memberships/<person_id>"
   Then I receive status code 200
    And membership timekeeper parameter contains the <boolean> value
Examples:
   |person_id |account_id | boolean |
   |3002807   |1033029    |true     |


  @crud
Scenario Outline: Verify that the user is able to remove from the account an existent membership
   Given A valid admin user token added on header
   When I do a "DEL" request with a person id <person_id> to pivotal endpoint "/accounts/<account_id>/memberships/<person_id>"
   Then I receive status code 204
Examples:
   |person_id |account_id |
   |3002807   |1033029    |