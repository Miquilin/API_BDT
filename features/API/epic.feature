Feature: Epic
  Verify operations on an individual epic an epic operations

@smoke @add_project_id @add_epic_id @admin
Scenario: GET an epic
  Given A valid admin user token added on header
  When I do a "GET" request with "epics" method to pivotal endpoint "/projects/{project_id}/epics/{epic_id}"
  Then I receive status code 200


@smoke @add_project_id @add_epic_id  @admin
Scenario: GET epic list
  Given A valid admin user token added on header
  When I do a "GET" request with "epics" method to pivotal endpoint "/projects/{project_id}/epics"
  Then I receive status code 200

@crud @add_project_id @add_epic_id @admin
Scenario: Verify that it is possible to get the details of an epic
  Given A valid admin user token added on header
  When I do a "GET" request with "epics" method to pivotal endpoint "/projects/{project_id}/epics/{epic_id}"
  Then I receive status code 200
    And Response has "id" parameter with right value
    And Response has "name" parameter with right value
    And Response has "kind" parameter with right value

@crud @add_project_id @add_epic_id @admin
Scenario: Verify that it is possible to get the details of an epic
  Given A valid admin user token added on header
  When I do a "GET" request with "epics" method to pivotal endpoint "/projects/{project_id}/epics/{epic_id}"
  Then I receive status code 200
    And Response has "id" parameter with right value
    And Response has "name" parameter with right value
    And Response has "kind" parameter with right value

@crud @add_project_id @add_epic_id @admin
Scenario: Verify that it is possible to delete an epic
  Given A valid admin user token added on header
    And There is an existent "epic"
  When I do a "DELETE" request with "epics" method to pivotal endpoint "/projects/{project_id}/epics/{epic_id}"
  Then I receive status code 204

@crud @add_project_id @add_epic_id @admin @edit
Scenario Outline: Verify that it is possible to update an epic
  Given A valid admin user token added on header
    And There is an existent "epic"
    And I need to "update" the "epic" with following <name_test>
  When I do a "PUT" request with "epics" method to pivotal endpoint "/projects/{project_id}/epics/{epic_id}"
  Then I receive status code 200
    And Response has new "name" parameter with right value

    Examples: updated name epic
        | name_test         |
        | Updated epic 1  |
        | Updated epic 2  |

@crud @add_project_id @admin @createnino
Scenario Outline: Verify that it is possible to create an epic
  Given A valid admin user token added on header
      And I need to "create" the "epic" with following <name_test>
  When I do a "POST" request with "epics" method to pivotal endpoint "/projects/{project_id}/epics"
  Then I receive status code 200
    And Response has "name" parameter with right value
    And Response has "kind" parameter with right value

    Examples: created name epic
        | name_test         |
        | Updated epic 1  |
        | Updated epic 2  |