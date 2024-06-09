import json

def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


festivals_with_time = read_json_objects_from_file(
    "festival_with_tuned_time_3.json")
festivals_full = read_json_objects_from_file(
    "refinedFestivalFromLehoiInfo_2.json")

for festival in festivals_full:
    for fes in festivals_with_time:
        if fes['name'] == festival['name']:
            festival["label"] = fes["chatgptName"]
            festival["start"] = fes["start"]
            festival["end"] = fes["end"]
            festival["lunarCalendar"] = fes["lunarCalendar"]
            break
    
with open('festival_with_tuned_time_4.json', 'w', encoding='utf-8') as file:
    json.dump(festivals_full, file, ensure_ascii=False)