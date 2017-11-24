import json

#Set values on a object like Project, Epic
def get_an_object_response(context, response, object_response):

    for key_name_aux, value_aux in response.items():
        context.logger.debug('key_name_aux: {}'.format(key_name_aux))
        context.logger.debug('value_aux: {}'.format(value_aux))
        if( type(value_aux) != "dict"):
            if (key_name_aux == "id"):
                object_response.set_id(int(value_aux))
            elif (key_name_aux == "name"):
                object_response.set_name(value_aux)
        else:
            for key_name_aux_1, value_aux_1 in value_aux.items():
                if (key_name_aux_1 == "id"):
                    object_response.set_id(int(value_aux_1))
                elif (value_aux_1 == "name"):
                    object_response.set_name(value_aux_1)
    return object_response

