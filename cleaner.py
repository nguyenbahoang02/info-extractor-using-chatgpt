import os
import json


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data

file_path = 'festival_with_raw_time/final.json'
json_objects = read_json_objects_from_file(file_path)
festivals = read_json_objects_from_file("refinedFestivalFromLehoiInfo_2.json")

cleaned_data = []

def check_exist(name):
    for obj in festivals:
        if obj["name"] == name:
            print(name)
            return True
    return False

for obj in json_objects:
    if check_exist(obj["name"]):
        cleaned_data.append(obj)


output_file = 'festival_with_raw_time/cleaned_data.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, indent=4, ensure_ascii=False)