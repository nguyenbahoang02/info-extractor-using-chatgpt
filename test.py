from handler.chatgpt_selenium_automation import ChatGPTAutomation
import json
import os
from itertools import dropwhile


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


json_objects = read_json_objects_from_file(
    "refinedFestivalFromLehoiInfo_2.json")
current_festivals = read_json_objects_from_file(
    "festival_with_raw_time/cleaned_data.json")


def check_exist(name):
    for fes in current_festivals:
        if fes['name'] == name:
            return True
    return False


chrome_driver_path = r"F:\Downloads\chromedriver-win64\chromedriver.exe"

chrome_path = r'"F:\Downloads\chrome-win64\chrome.exe"'

chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

for obj in json_objects:
    if not check_exist(obj['name']):
        try:
            print(obj['name'])
            description = obj['description']
            prompt = "Hãy trích xuất tên lễ hội và thời gian(nếu lễ hội kết thúc trong 1 ngày thì thời gian bắt đầu bằng kết thúc) từ mô tả sau(không được bịa thông tin) ?" + description.replace(
                "'", " ") + "Hãy trả lời dưới dạng 1 json object. Ví dụ: {name: Lễ hội Giã La,time :{start: 6/1,end: 14/1,lunarCalendar: True(False nếu là ngày dương lịch)}}" + "Bạn không cần phải giải thích 1 điều gì chỉ cần trả về 1 json object là được VÀ HÃY TRẢ LỜI Ở DẠNG RAW TEXT(không được bọc trong thẻ code và thuộc tính của jsonobject để trong dấu nháy kép)"
            chatgpt.send_prompt_to_chatgpt(prompt)
            response = chatgpt.return_last_response()
            print(response)
            json_string = response[response.index('{'):response.rindex('}')+1]
            modified_string = json_string.replace("'", '"').replace(
                "'", "\'").replace("ChatGPT\n", "")
            print(modified_string)
            json_object = json.loads(modified_string)
            print(json_object)
            current_festivals.append({
                'name': obj['name'],
                'chatgptName': json_object['name'],
                'start': json_object['time']['start'],
                'end': json_object['time']['end'],
                'lunarCalendar': json_object['time']['lunarCalendar']
            })
        except Exception as e:
            print(e)
            print('\n')

with open('festival_with_raw_time/cleaned_data.json', 'w', encoding='utf-8') as file:
    json.dump(current_festivals, file, ensure_ascii=False)
