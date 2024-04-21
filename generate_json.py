import json

# This is the original JSON object
original_json = {
    "user_id": "661e5a845d265411cef8526f",
    "hire_type": "FREELANEER",
    "hire_freelaneer": {
        "details": {
            "project_title": "Create a MERN Web Project for Food Delivery System - Y Dev Client",
            "project_description": "Experience seamless food delivery with our MERN-based platform. Browse restaurants, place orders, and track deliveries effortlessly. For customers, it's convenience at your fingertips. For restaurants, it's streamlined operations and increased reach. Join us and savor the future of food delivery!",
            "project_size": "SMALL_PROJECT",
            "project_urgency": "MORE_THAN_2_WEEKS"
        },
        "speciality": {
            "category": {
                "category_id": "660ccf89951b4128550cb716",
                "category_name": "Development & IT"
            },
            "sub_category": {
                "subcategory_id": "660cd537951b4128550cb73c",
                "subcategory_name": "Web Development"
            },
            "skills": [
                {
                    "id": "660cd8dc7b24e2ab44065114",
                    "name": "TypeScript"
                },
                {
                    "id": "660cd8f77b24e2ab44065117",
                    "name": "Node Js"
                }
            ]
        },
        "attachments": {
            "files": [
                {
                    "id": "c7eae831-8062-4302-acbe-1dd73d5d4e16",
                    "name": "Project_Request_Documentation.pdf",
                    "size": "15055",
                    "type": "application/pdf",
                    "url": "https://freelaneer.s3.us-east-1.amazonaws.com/1705312440256-Project_Request_Documentation.pdf"
                }
            ],
            "links": [
                {
                    "name": "Project Guidelines",
                    "url": "https://example.com/guidelines"
                }
            ]
        },
        "payment": {
            "payment_frequency": "TIME_FRAME",
            "time_frame_type": "WEEKLY",
            "time_frame_weekly": {
                "number_of_weeks": 4,
                "payment_per_week": 500
            },
            "total_budget": 2000,
            "revision": 2
        }
    },
    "job_status": "OPEN"
}

# Create a list to hold the new JSON objects
new_json_objects = []

# Generate 100 new JSON objects
for i in range(1, 201):
    # Copy the original JSON object
    new_json = json.loads(json.dumps(original_json))
    
    # Change the project_title and project_description
    new_json["hire_freelaneer"]["details"]["project_title"] = f"New Title {i}"
    new_json["hire_freelaneer"]["details"]["project_description"] = f"New Description {i}"
    
    # Add the new JSON object to the list
    new_json_objects.append(new_json)

# Convert the list of JSON objects to a JSON string
json_string = json.dumps(new_json_objects, indent=4)

# Print the JSON string
print(json_string)