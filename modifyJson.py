import random
from generate_random_sentence import generate_random_sentence
from generate_random_id import generate_random_id

def modify_json(new_json, i):
    # Change user_id
    new_json["user_id"] = generate_random_id(24)
    
    # Generate a random sentence and add it to the project_title
    new_json["hire_freelaneer"]["details"]["project_title"] = generate_random_sentence(5, 10)
    
    # Generate a random sentence and add it to the project_description
    new_json["hire_freelaneer"]["details"]["project_description"] = generate_random_sentence(50, 100)
    
    # Change project_size, project_urgency, category_id, subcategory_id
    new_json["hire_freelaneer"]["details"]["project_size"] = generate_random_sentence(1, 3)
    new_json["hire_freelaneer"]["details"]["project_urgency"] = generate_random_sentence(1, 5)
    new_json["hire_freelaneer"]["speciality"]["category"]["category_id"] = generate_random_id(24)
    new_json["hire_freelaneer"]["speciality"]["sub_category"]["subcategory_id"] = generate_random_id(24)
    
    # Change category_name, subcategory_name, skills.id, skills.name
    new_json["hire_freelaneer"]["speciality"]["category"]["category_name"] = generate_random_sentence(1, 3)
    new_json["hire_freelaneer"]["speciality"]["sub_category"]["subcategory_name"] = generate_random_sentence(1, 3)
    for skill in new_json["hire_freelaneer"]["speciality"]["skills"]:
        skill["id"] = generate_random_id(24)
        skill["name"] = generate_random_sentence(1, 3)
    
    # Change files.id, files.name, files.size
    for file_info in new_json["hire_freelaneer"]["attachments"]["files"]:
        file_info["id"] = generate_random_id(36)
        file_info["name"] = generate_random_sentence(1, 3)
        file_info["size"] = str(random.randint(10000, 50000))
    
    # Change links.name
    for link in new_json["hire_freelaneer"]["attachments"]["links"]:
        link["name"] = generate_random_sentence(1, 3)
    
    # Change payment_frequency, time_frame_type, number_of_weeks, payment_per_week, total_budget, revision
    new_json["hire_freelaneer"]["payment"]["payment_frequency"] = generate_random_sentence(1, 5)
    new_json["hire_freelaneer"]["payment"]["time_frame_type"] = generate_random_sentence(1, 4)
    new_json["hire_freelaneer"]["payment"]["time_frame_weekly"]["number_of_weeks"] = random.randint(1, 10)
    new_json["hire_freelaneer"]["payment"]["time_frame_weekly"]["payment_per_week"] = random.randint(100, 1000)
    new_json["hire_freelaneer"]["payment"]["total_budget"] = random.randint(1000, 10000)
    new_json["hire_freelaneer"]["payment"]["revision"] = random.randint(1, 5)
    
    # Change job_status
    new_json["job_status"] = generate_random_sentence(1, 3)
    
    return new_json