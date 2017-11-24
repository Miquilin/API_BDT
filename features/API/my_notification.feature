Feature: My Notification
  Return list of the notifications for the auhenticated person. Response is sorted by notification created_at most recent first.

@smoke
Scenario: GET a response
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/my/notifications"
  Then I receive status code 200






