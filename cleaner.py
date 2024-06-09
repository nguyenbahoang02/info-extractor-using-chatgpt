import os
import json


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


festivals = read_json_objects_from_file(
    'festival_historical_figure/final.json')
# festivals = read_json_objects_from_file("refinedFestivalFromLehoiInfo_2.json")

cleaned_data = []


# def check_exist(name):
#     for obj in festivals:
#         if obj["name"] == name:
#             # print(name)
#             return True
#     return False


for festival in festivals:
    # if check_exist(obj["name"]):
    if festival["thờ"] != None:
        cleaned_data.append(festival)


output_file = 'festival_historical_figure/cleaned_data.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(cleaned_data, file, indent=4, ensure_ascii=False)
