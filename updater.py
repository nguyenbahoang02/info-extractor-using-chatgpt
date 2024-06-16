import json

def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data

festivals = read_json_objects_from_file("festival_final_time.json")

final_festivals = []
for festival in festivals:
    new_fes = festival
    if "startDay" not in festival and "endDay" not in festival and "startMonth" not in festival and "endMonth" not in festival and "startYear" not in festival and "endYear" not in festival:
        del(new_fes["lunarCalendar"])
    if "startDay" in festival:
        new_fes["startDay"] = str(new_fes["startDay"]).zfill(2)
    if "startMonth" in festival:
        new_fes["startMonth"] = str(new_fes["startMonth"]).zfill(2)
    if "startYear" in festival:
        new_fes["startYear"] = str(new_fes["startYear"]).zfill(4)
    if "endDay" in festival:
        new_fes["endDay"] = str(new_fes["endDay"]).zfill(2)
    if "endMonth" in festival:
        new_fes["endMonth"] = str(new_fes["endMonth"]).zfill(2)
    if "endYear" in festival:
        new_fes["endYear"] = str(new_fes["endYear"]).zfill(4)
    # if festival["start"] != None:
    #     if "day" in festival["start"]:
    #         if festival["start"]["day"] != None:
    #             new_fes["startDay"] = festival["start"]["day"]
    #     if "month" in festival["start"]:
    #         if festival["start"]["month"] != None:
    #             new_fes["startMonth"] = festival["start"]["month"]
    #     if "year" in festival["start"]:
    #         if festival["start"]["year"] != None:
    #             new_fes["startYear"] = festival["start"]["year"]
    # if festival["end"] != None:
    #     if "day" in festival["end"]:
    #         if festival["end"]["day"] != None:
    #             new_fes["endDay"] = festival["end"]["day"]
    #     if "month" in festival["end"]:
    #         if festival["end"]["month"] != None:
    #             new_fes["endMonth"] = festival["end"]["month"]
    #     if "year" in festival["end"]:
    #         if festival["end"]["year"] != None:
    #             new_fes["endYear"] = festival["end"]["year"]
    # del(new_fes["start"])
    # del(new_fes["end"])
    final_festivals.append(new_fes)

with open("festival_final_time_1.json", 'w', encoding='utf-8') as file:
    json.dump(final_festivals, file, indent=4, ensure_ascii=False)