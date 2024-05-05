import os
import json


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data

file_path = 'relation/final.json'
json_objects = read_json_objects_from_file(file_path)

cleaned_data = []

for obj in json_objects:
    if 'liên hệ' not in obj:
        continue
    if obj['liên hệ'] == None:
        continue
    cleaned_data.append(obj)


output_file = 'relation/cleaned_data_1.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, indent=4, ensure_ascii=False)