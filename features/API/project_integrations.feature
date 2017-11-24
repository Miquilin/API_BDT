Feature: Project Integration
Successful responses to this request return an array containing zero or more instances of an integration-type resource. In particular, any mix of any of the following: bugzilla_integration, get_satisfaction_integration, jira_integration, lighthouse_integration, other_integration, zendesk_integration.

  @smoke
Scenario Outline: Verify the status code is 200 when a request for project's integrations is sent
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/projects/<Project>/integrations"
  Then I receive a integration list
    Examples:
    |Project|
    |2131315|