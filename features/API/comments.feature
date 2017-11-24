#Feature: comments
#  Returns the specified story's comments.
#
#@smoke
#Scenario:
#  Given A valid admin user token added on header
#  When I do a "GET" request to pivotal endpoint "/projects/2123257/stories/152312720/comments"
#  Then I receive status code 200