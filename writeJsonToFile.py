import json
from generateJson import generate_new_json_objects
from amountOfData import num_objects

def write_json_to_file(json_object, filename):
    with open(filename, 'w') as f:
        # Convert the list of JSON objects to a JSON string
        json.dump(json_object, f, indent=4)

new_json_objects = generate_new_json_objects(num_objects)
write_json_to_file(new_json_objects, 'generatedDummyData.json')