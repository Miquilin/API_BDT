Feature: Epic
  Verify operations on an individual epic an epic operations

@smoke
Scenario: GET an epic
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "epic"
  When I do a "GET" request with parameters to pivotal endpoint "/projects/{project_id}/epics/{epic_id}"
  Then I receive status code 200


@smoke
Scenario: GET epic list
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "epics"
  When I do a "GET" request with parameters to pivotal endpoint "/projects/{project_id}/epics"
  Then I receive status code 200





