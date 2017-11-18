Feature: me
  Provides information about the authenticated user.

@smoke
Scenario:
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/me"
  Then I receive status code 200






