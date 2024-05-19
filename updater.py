import json

def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data

hf_titles = read_json_objects_from_file("title/cleaned_data.json")
hfs = read_json_objects_from_file("HFFromWikipediaWithRelation_1.json")

for hf_title in hf_titles:
    for hf in hfs:
        if hf["name"] == hf_title["name"]:
                hf["positionTitle"] = hf_title["chức vụ"]
                break

output_file = 'HFFromWikipediaWithRelation_2.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(hfs, file, indent=4, ensure_ascii=False)