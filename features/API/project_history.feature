Feature: Project History
Returns per day information of story points and counts by state. If no start date or end date is provided, the project's most recent history is returned. If only an end date is provided, the start date will be automatically calculated. The daily history represents the state of the project's stories at midnight in the project's timezone.

@smoke
Scenario Outline: Verify the status code is 200 when a request for a list of snapshots of a project is sent
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/projects/<Project>/history/days"
  Then I receive a history dictionary
  Examples:
  |Project|
  |2131315|