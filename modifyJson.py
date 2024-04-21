def modify_json(new_json, i):
    # Change the project_title and project_description
    new_json["hire_freelaneer"]["details"]["project_title"] = f"New Title {i}"
    new_json["hire_freelaneer"]["details"]["project_description"] = f"New Description {i}"
    return new_json