Feature: Iterations
Allows iterations to be retrieved, with optional scope, limit and offset.
For the 'Done' scope, a negative offset can be passed, which specifies the number of iterations preceding the 'Current' iteration.
Note that iterations are ordered with the oldest (lowest iteration number) first.


@smoke
Scenario: Iterations list
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "iterations"
  When I do a "GET" request with parameters to pivotal endpoint "/projects/{project_id}/iterations"
  Then I receive status code 200