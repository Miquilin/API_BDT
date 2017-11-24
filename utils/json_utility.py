import json

class JsonUtility:

    def __init__(self):
        self.result = []

    def search_item(self, dictionary, parameter):
        """" Recursively search for the parameter provided into the dictionary."""
        for key, value in dictionary.items():
            if isinstance(value, str):
                if key == parameter:
                    self.result.append(value)
            elif isinstance(value, int):
                if key == parameter:
                    self.result.append(value)
            elif isinstance(value, unicode):
                if key == parameter:
                    self.result.append(value)
            else:
                self.search_item(value, parameter)
        return self.result


    def read_json_from_file(self, filename):
        """Read a json file and convert it to dictionary"""
        path = "../../data/" + filename
        with open (path) as json_data:
            data = json.load(json_data)
            json_data.close()
        return data

    def get_json_from_file(self, filename):
        """Read a json file and returns it"""
        path = "../../data/" + filename
        datafile= open(path, "r")
        data = str(datafile.read()) # lee el contenido del archivo
        return data