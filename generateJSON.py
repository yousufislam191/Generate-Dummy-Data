import json
from modifyJson import modify_json

def generate_new_json_objects(num_objects):
    with open('sampleData.json') as f:
        original_json = json.load(f)

    # Create a list to hold the new JSON objects
    new_json_objects = []

    # Generate 100 new JSON objects
    for i in range(1, num_objects + 1):
        # Copy the original JSON object
        new_json = json.loads(json.dumps(original_json))
        new_json = modify_json(new_json, i)
        
         # Add the new JSON object to the list
        new_json_objects.append(new_json)

    return new_json_objects