Feature: Projects
  Access the project specified by the project_id value in the URL. Access a user's projects

  @smoke
  Scenario: Get all projects
    Given A valid admin user token added on header
    When I do a "GET" request to pivotal endpoint "/projects"
    Then I receive a projects list

  @smoke
  Scenario Outline: Verify the status code is 200 when a request for a project is sent
    Given A valid admin user token added on header
    When I do a "GET" request to pivotal endpoint "/projects/<Project>"
    Then I receive status code 200
    And I receive a project as result
    Examples:
      | Project |
      | 2131050 |
      | 2131310 |

  @crud
  Scenario Outline: Verify it is possible to create a new project
    Given A valid admin user token added on header
    And I have "name" with value "<name>"
    And I have "week_start_day" with value "<week_start_day>"
    And I have "project_type" with value "<project_type>"
    And I have "join_as" with value "<join_as>"
    When I do a "POST" request to pivotal endpoint "/projects"
    Then I receive new object created
    And I receive status code 200
    Examples:
      |name|week_start_day|project_type|join_as|
      |RPFH proy|Monday   |demo       |owner  |
      |New RPFH |Monday   |private |owner  |
      |Another|Monday  |shared      |owner |
      |AnotherM|Monday  |public      |owner |


  @crud
  Scenario Outline: Verify it is possible to update a project
    Given A valid admin user token added on header
    And I have "name" with value "<name>"
    And I have "description" with value "<description>"
    When I do a "PUT" request to pivotal endpoint "/projects/<ID>"
    Then I receive new object created
    And I receive status code 200
    Examples:
      | ID      | name               | description|
      | 2131310 | Editing my project | My description|


  @crud
Scenario Outline: Verify it is possible to delete a project
  Given A valid admin user token added on header
  When I do a "DELETE" request to pivotal endpoint "/projects/<Project>"
    Then I receive new object created
    And I receive status code 200
  Examples:
    |Project|
    |2131580|
    |2131579|
    |2131576|