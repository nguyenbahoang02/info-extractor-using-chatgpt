import json


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


festivals_with_only_relation = read_json_objects_from_file(
    "festival_historical_figure/festival_final_time.json")
festivals = read_json_objects_from_file(
    "festival_historical_figure/cleaned_data.json")

for festival in festivals_with_only_relation:
    for fes in festivals:
        if fes["name"] == festival["name"]:
            fes["commemorate"] = festival[""]

output_file = 'HFFromWikipediaWithRelation_3.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(historical_figures, file, indent=4, ensure_ascii=False)
