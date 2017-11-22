Feature: Project Webhooks
Lets the user access the project's list of webhooks.

@smoke
Scenario: Verify the status code is 200 when a  request for a list of webhooks in a project is sent
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/projects/2122997/webhooks"
  Then I receive status code 200