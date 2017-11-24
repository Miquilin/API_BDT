Feature: Story tasks

@dani
Scenario: GET  Story task
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "task"
  When I do a "GET" request to pivotal endpoint "/projects/2122997/stories/152312174/tasks/58941826"
  Then I receive status code 200



@dani
Scenario: GET stories  tasks
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "tareas"
  When I do a "GET" request to pivotal endpoint "/projects/2122997/stories/152312174/tasks"
  Then I receive status code 200