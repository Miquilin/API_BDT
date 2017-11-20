class Project:
    def __init__(self):
        self.project_id = "0"
        self.name = "None"

    def get_project_id(self):
        return self.project_id

    def get_name(self):
        return self.name

    def set_project_id(self, project_id):
        self.project_id=project_id

    def set_name(self, name):
        self.name = name

