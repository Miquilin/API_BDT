Feature: Projects
Access the project specified by the project_id value in the URL. Access a user's projects

@project
Scenario: Get all projects
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/projects"
  Then I receive projects list


#@get_list
#Scenario: Verify the status code is 200 when a  request for a list of active users in a project is sent
#  Given A valid admin user token added on header
#  When I do a "GET" request to pivotal endpoint "/projects"
#  Then I receive status code 200

@project
Scenario: Verify the status code is 200 when a request for a project is sent
  Given A valid admin user token added on header
  When I do a "GET" request to pivotal endpoint "/projects/2122997"
  Then I receive status code 200

#@crud @creates
#Scenario: Verify it is possible to create a project
#  Given A valid admin user token added on header
#  And I will create project "My New Project"
#  When I sending a "POST" request to pivotal endpoint "/projects"
#  Then I receive status code 200
#  And I receive the project id
#
#@updates
#Scenario Outline: Verify it is possible to update a project
#  Given A valid user user token added on header
#  And I have the project <ID>
#  And I need to update the project name to <Name>
#  And I need to update the project description to <Description>
#  When I do a "PUT" request to pivotal endpoint "/projects/2122997"
#  Then I receive status code 200
#Examples:
#  |ID|Name|Description|
#  |123456|Editing my project|This my descrption|
#
#@crud @deletes
#Scenario: Verify it is possible to delete a project
#  Given A valid admin user token added on header
#  And I will delete project 123123
#  When I do a "DELETE" request to pivotal endpoint "/projects/2122997"
#  Then I receive status code 200