Feature: comments
  Returns the specified story's comments.

@smoke
Scenario Outline:
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/projects/<project_id>/stories/<us_id>/comments"
  Then I receive status code 200
  Examples:
    |project_id |us_id      |
    |2130313     |153054113 |