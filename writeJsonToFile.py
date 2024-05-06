import json
import time
from generateJSON import generate_new_json_objects
from amountOfData import num_objects

def write_json_to_file(json_object, filename):
    with open(filename, 'w') as f:
        # Convert the list of JSON objects to a JSON string
        json.dump(json_object, f, indent=4)

start_time = time.time()

new_json_objects = generate_new_json_objects(num_objects)
write_json_to_file(new_json_objects, 'generatedDummyData.json')

end_time = time.time()

print(f"Execution time of the program is: {end_time - start_time} seconds")
print(f"Number of JSON objects created: {len(new_json_objects)}")