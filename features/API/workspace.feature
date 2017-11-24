Feature:  something

@dani
Scenario: GET workspaces
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "workspaces"
  When I do a "GET" request to pivotal endpoint "/my/workspaces"
  Then I receive status code 200

