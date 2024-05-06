# import json
# import time
# from generateJSON import generate_new_json_objects
# from amountOfData import num_objects

# def write_json_to_file(json_object, filename):
#     with open(filename, 'w') as f:
#         # Convert the list of JSON objects to a JSON string
#         json.dump(json_object, f, indent=4)

# start_time = time.time()

# new_json_objects = generate_new_json_objects(num_objects)
# write_json_to_file(new_json_objects, 'generatedDummyData.json')

# end_time = time.time()

# print(f"Execution time of the program is: {end_time - start_time} seconds")
# print(f"Number of JSON objects created: {len(new_json_objects)}")


#TODO: Reduced memory uses by implementing batch processing and streaming output. This code is more efficient than the previous version. The code writes the JSON objects to a file in batches of 1000 objects. The code also calculates the completion percentage of the program and prints it to the console. The program execution time is also printed to the console. The generatedDummyData.json file is downloaded after the program completes execution.

#TODO: This code is more efficient for generating million amount of dummy data.


import json
import time
from generateJSON import generate_new_json_objects
from amountOfData import num_objects
# from google.colab import files

def write_json_to_file(json_objects, filename):
    with open(filename, 'a') as f:
        for json_object in json_objects:
            json.dump(json_object, f, indent=4)
            f.write('\n')

batch_size = 1000
start_time = time.time()

for i in range(0, num_objects, batch_size):
    batch_json_objects = generate_new_json_objects(batch_size)
    write_json_to_file(batch_json_objects, 'generatedDummyData.json')
    
    # Calculate completion percentage
    completion_percentage = min((i + batch_size) / num_objects * 100, 100)
    print(f"Completion: {completion_percentage:.2f}%")

end_time = time.time()

print(f"Execution time of the program is: {end_time - start_time} seconds")

# Download the generatedDummyData.json file
# files.download('generatedDummyData.json')
