import json


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


historical_figures_with_only_relation = read_json_objects_from_file(
    "relation/cleaned_data.json")
historical_figures = read_json_objects_from_file(
    "HFFromWikipediaWithRelation_2.json")


# def check_exist(title_name):
#     for obj in title_with_description:
#         if obj["name"] == title_name:
#             print(title_name)
#             return True
#     return False


for historical_figure in historical_figures_with_only_relation:
    for hf in historical_figures:
        if hf["name"] == historical_figure["name"]:
            for relation in historical_figure["liên hệ"]:
                if relation["loại"] not in hf:
                    hf[relation["loại"]] = []
                if not isinstance(hf[relation["loại"]], list):
                    hf[relation["loại"]] = []
                hf[relation["loại"]].append(relation["tên"])

output_file = 'HFFromWikipediaWithRelation_3.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(historical_figures, file, indent=4, ensure_ascii=False)
