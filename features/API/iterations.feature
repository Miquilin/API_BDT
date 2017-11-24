Feature: Iterations
Allows iterations to be retrieved, with optional scope, limit and offset.
For the 'Done' scope, a negative offset can be passed, which specifies the number of iterations preceding the 'Current' iteration.
Note that iterations are ordered with the oldest (lowest iteration number) first.


@smoke @add_project_id @admin
Scenario: Iterations list
  Given A valid admin user token added on header
  When I do a "GET" request with "iterations" method to pivotal endpoint "/projects/{project_id}/iterations"
  Then I receive status code 200


