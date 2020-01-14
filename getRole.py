import json

# Fakes an Aurora MySQL Data API Response
# from 'SELECT * FROM Role WHERE RoleID = 1;'
def execute_statment(sql):
    json_file = open("getRole_actual.json", 'r')
    json_response = json_file.read()
    response = json.loads(json_response)
    return response

# Query the Aurora MySQL database
response = execute_statment('SELECT * FROM Role WHERE RoleID = 1;')

# Merge values with labels
formatted_response = label_values(response['records'], response['columnMetadata'])

# Output the response as JSON
output = json.dumps(formatted_response)

# See getRole_desired.json for example
print(output)
