import json
from generateJSON import generate_new_json_objects

def write_json_to_file(json_object, filename):
    with open(filename, 'w') as f:
        # Convert the list of JSON objects to a JSON string
        json.dump(json_object, f, indent=4)

new_json_objects = generate_new_json_objects(200)
write_json_to_file(new_json_objects, 'output.json')