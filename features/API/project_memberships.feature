Feature: Project Membership
Membership operations.

@smoke
Scenario Outline: Verify the status code is 200 when a  request for a list of membership in a project is sent
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/projects/<Project>/memberships"
  Then I receive status code 200
  And I receive a memberships list
  Examples:
  | Project|
  | 2131315|
