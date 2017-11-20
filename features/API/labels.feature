Feature: Labels
Access the project's labels.


@smoke
Scenario: GET list Labels
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "labels"
  When I do a "GET" request with parameters to pivotal endpoint "/projects/{project_id}/labels"
  Then I receive status code 200