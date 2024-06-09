import json
import os
import re
from itertools import dropwhile


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


festivals = read_json_objects_from_file(
    "festival_with_raw_time/cleaned_data.json")
current_festivals = read_json_objects_from_file(
    "festival_with_tuned_time_2.json")

# fes = []

# def check_exist(name):
#     for fes in current_festivals:
#         if fes['name'] == name:
#             return True
#     return False


for festival in festivals:
    for fes in current_festivals:
        if fes['name'] == festival['name']:
            festival["start"] = fes["start"]
            festival["end"] = fes["end"]
            break


with open('festival_with_tuned_time_3.json', 'w', encoding='utf-8') as file:
    json.dump(festivals, file, ensure_ascii=False)
