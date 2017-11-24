from json import loads

'''This method turns the response into a list'''


def getting_list(context, service):
    gral_data = {}
    dict_response = loads(context.result.text)
    if len(dict_response) > 0:
        i = 0
        for i in range(len(dict_response)):
            convert = dict_response[i]
            gral_data[i] = convert
    filename = "../API_BDT/data/" + service + ".json"
    create_file(gral_data, filename)
    return gral_data


'''This method turns the response into a dictionary'''


def getting_dict(context, service):
    gral_data = {}
    dict_response = loads(context.result.text)
    if len(dict_response) > 0:
        i = 0
        for i in range(len(dict_response)):
            convert = dict_response.get(i)
            gral_data[i] = convert
    filename = "../API_BDT/data/" + service + ".json"
    create_file(gral_data, filename)
    return gral_data


'''This method returns an object'''


def getting_object(context, service):
    dict_response = context.result.text
    for keys, values in dict(loads(dict_response)).items():
        print('\t\t',keys, '::', values)
    an_object = []
    an_object.append(dict_response)
    filename = "../API_BDT/data/" + service + ".json"
    #create_file(an_object, filename)
    return an_object


''' Writes data into a JSON file'''


def create_file(object, file):
    file_object = open(file, "w")
    i = 0
    for i in range(len(object)):
        file_object.write(str(object[i]))
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
