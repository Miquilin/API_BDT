Feature: Project Membership
Membership operations.

@smoke
Scenario: Verify the status code is 200 when a  request for a list of membership in a project is sent
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/projects/2122997/memberships"
  Then I receive status code 200