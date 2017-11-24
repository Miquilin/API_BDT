class Response:
    def __init__(self,status_code, content ):
        self.status_code = status_code
        self.content = content

    def get_status_code(self):
        return self.status_code

    def set_status_code(self, status_code):
        self.status_code = status_code


    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content