Feature: Story tasks

@dani
Scenario: GET  Story task
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "task"
  When I do a "GET" request to pivotal endpoint "/projects/2130313/stories/153137131/tasks/59352620"
  Then I receive status code 200



@dani
Scenario: GET stories  tasks
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "tareas"
  When I do a "GET" request to pivotal endpoint "/projects/2130313/stories/153137131/tasks"
  Then I receive status code 200