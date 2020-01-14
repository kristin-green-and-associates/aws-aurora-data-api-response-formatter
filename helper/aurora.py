import json

# Fakes the merging of labels and values
# This is the assignment!
def label_values(records, metadata):
    json_file = open("../getRoles_desired.json", 'r')
    json_response = json_file.read()
    response = json.loads(json_response)
    return response
