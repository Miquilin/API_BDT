Feature: Story

@dani
Scenario: GET an story
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "story"
  When I do a "GET" request to pivotal endpoint "/projects/2130313/stories/153137131"
  Then I receive status code 200



@dani
Scenario: GET stories list
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "stories"
  When I do a "GET" request to pivotal endpoint "/projects/2130313/stories"
  Then I receive status code 200

@dani
Scenario: GET stories bulk list
  Given A valid admin user token added on header
    And The user has an existent test "project" with existent(s) "bulk"
  When I do a "GET" request to pivotal endpoint "/projects/2130313/stories/bulk"
  Then I receive status code 400





