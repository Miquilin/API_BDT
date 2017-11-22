from utils.tool_project import *

def main():
    tool_project_test= tool_project("admin","test 2123")
    print(tool_project_test.create_project_test().status_code)
    tool_project_test.get_all_project()
    tool_project_test.get_a_project_by_name("Miquilin Project")

main()