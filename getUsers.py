import json
from helper.aurora import label_values

# Fakes an Aurora MySQL Data API Response
# from 'SELECT * FROM User;'
def execute_statment(sql):
    json_file = open("getUsers_actual.json", 'r')
    json_response = json_file.read()
    response = json.loads(json_response)
    return response

# Query the Aurora MySQL database
response = execute_statment('SELECT * FROM User;')

# Merge values with labels
formatted_response = label_values(response['records'], response['columnMetadata'])

# Output the response as JSON
output = json.dumps(formatted_response)

# See getRoles_desired.json for example
print(output)
