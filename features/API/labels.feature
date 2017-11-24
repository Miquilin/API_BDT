Feature: Labels
Access the project's labels.


@smoke @add_project_id @admin
Scenario: GET list Labels
  Given A valid admin user token added on header
  When I do a "GET" request with "labels" method to pivotal endpoint "/projects/{project_id}/labels"
  Then I receive status code 200

