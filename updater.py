import json

def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data

festivals_relations = read_json_objects_from_file("FinalFestival.json")
festivals_full = read_json_objects_from_file("festival_final_time_copy.json")

for festival in festivals_relations:
    for fest in festivals_full:
        if festival["name"] == fest["name"]:
            fest["commemorate"] = festival["thờ"]
            break



with open("FinalFestival_1.json", 'w', encoding='utf-8') as file:
    json.dump(festivals_full, file, indent=4, ensure_ascii=False)