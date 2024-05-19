import json


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


title_with_description = read_json_objects_from_file("newTitles.json")
titles = read_json_objects_from_file("title/cleaned_data.json")


def check_exist(title_name):
    for obj in title_with_description:
        if obj["name"] == title_name:
            print(title_name)
            return True
    return False


for title in titles:
    for title_obj in title["chức vụ"]:
        if not check_exist(title_obj):
            title_with_description.append({"name": title_obj})

output_file = 'newTitles_1.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(title_with_description, file, indent=4, ensure_ascii=False)
