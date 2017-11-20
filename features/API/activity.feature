Feature: activity
  Return list of activity for the authenticated person. (Paginated).

@smoke
Scenario:
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/my/activity"
  Then I receive status code 200