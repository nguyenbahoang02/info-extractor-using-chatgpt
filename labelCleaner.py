import json

def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data

query_result = read_json_objects_from_file("queryResults.json")

labels = []

for Xlabel in query_result["results"]["bindings"]:
    labels.append(Xlabel["XLabel"]["value"])

output_file = 'labels.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(labels, file, indent=4, ensure_ascii=False)