import json
from originalJSON import original_json

def generate_new_json_objects(num_objects):
    # Create a list to hold the new JSON objects
    new_json_objects = []

    # Generate 100 new JSON objects
    for i in range(1, num_objects + 1):
        # Copy the original JSON object
        new_json = json.loads(json.dumps(original_json))
        
        # Change the project_title and project_description
        new_json["hire_freelaneer"]["details"]["project_title"] = f"New Title {i}"
        new_json["hire_freelaneer"]["details"]["project_description"] = f"New Description {i}"
        
         # Add the new JSON object to the list
        new_json_objects.append(new_json)

    return new_json_objects