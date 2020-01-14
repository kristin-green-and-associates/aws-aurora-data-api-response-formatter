import json

def label_values(records, metadata):

    labels = list() # labels list
    values = list() # vaules list
    response = list() # converted data

    #Get keys
    for p in metadata:
        labels.append(p['label'])

    #Get Values
    for p in records:
        temp_values = list()
        for q in p:
            for key, value in q.items():
                temp_values.append(value)
        values.append(temp_values)

    #combine key and values
    for p in values:
        response.append(dict (zip (labels, p)))

    return response
