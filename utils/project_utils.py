import requests
from json import load, loads, JSONDecoder, JSONEncoder, dumps

'''This method turns the response into a dictionary'''
def printing_response(context,file):
        # printing the response as is
        filename = "../API_BDT/Data/" + file+".json"
        #print (context.result.text)
        projects = loads(context.result.text)
        i=0
        for i in range (len(projects)):
                print ("\n.................................................................................\n")
                convertido = dumps(projects[i]) # Convierte en un json
                project = loads(convertido) # Convierte de json a diccionario
                #print (dict(project)) # Imprime un diccionario
                project_keys = dict(project).keys() # Recupera los keys de un diccionario
                print (project_keys)


def create_file(projects,file):
        file_object = open(file, "w")
        i = 0
        for i in range(len(projects)):
            file_object.write(str(projects[i]))
            file_object.write("\n.................................................................................\n")
        file_object.close()


'''
#specify url
url = 'my URL'

project_data = {
        "name": "New name",
        "description": "Changed Description",
        }

headers = {'Authorization': 'Bearer ' + token, "Content-Type": "application/json", 'data':project_data}

#Call REST API
response = requests.put(url, data=project_data, headers=headers)

#Print Response
print(response.text)
'''