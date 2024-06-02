import json


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


title_with_description = read_json_objects_from_file(
    "festival_with_raw_time/extracted_using_chatgpt_37.json")
titles = read_json_objects_from_file("festival_with_raw_time/final.json")


# def check_exist(title_name):
#     for obj in title_with_description:
#         if obj["name"] == title_name:
#             print(title_name)
#             return True
#     return False


for title in title_with_description:
    titles.append(title)

output_file = 'festival_with_raw_time/final.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(titles, file, indent=4, ensure_ascii=False)
