from handler.chatgpt_selenium_automation import ChatGPTAutomation
import json
import os
import re
from itertools import dropwhile


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


def check_year_followed_by_quote(json_like_str):
    # Define the regex pattern to check for "year" followed by a quotation mark
    pattern = re.compile(r'"year"\s*:\s*"\s*')

    # Search for the pattern in the input string
    match = pattern.search(json_like_str)

    # Return True if pattern is found, else False
    return match is not None


festivals = read_json_objects_from_file(
    "festival_with_raw_time/cleaned_data.json")
current_festivals = read_json_objects_from_file(
    "festival_with_tuned_time_2.json")


def check_exist(name):
    for fes in current_festivals:
        if fes['name'] == name:
            return True
    return False


chrome_driver_path = r"F:\Downloads\chromedriver-win64\chromedriver.exe"

chrome_path = r'"F:\Downloads\chrome-win64\chrome.exe"'

chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

for obj in festivals:
    if not check_exist(obj['name']):
        try:
            print(obj['name'])
            start = obj['start']
            end = obj["end"]
            prompt = "Hãy viết lại thời gian dưới đây dưới dạng chuẩn start:" + start \
                + "end: " + end + "Hãy trả lời dưới dạng 1 json object. Ví dụ: {start: {day:1,month: 6,year: null},end: {day:3,month: 6,year: null}}" + \
                "Bạn không cần phải giải thích 1 điều gì chỉ cần trả về 1 json object là được VÀ HÃY TRẢ LỜI Ở DẠNG RAW TEXT(không được bọc trong thẻ code và thuộc tính của jsonobject để trong dấu nháy kép, thông tin nào không có thì để null, không được bỏ trống, PHẢI CÓ DẤU : SAU TÊN THUỘC TÍNH)"
            chatgpt.send_prompt_to_chatgpt(prompt)
            response = chatgpt.return_last_response()
            print(response)
            json_string = response[response.index('{'):response.rindex('}')+1]
            modified_string = json_string.replace("'", '"').replace(
                "'", "\'").replace("ChatGPT\n", "")
            print(modified_string)
            # if not check_year_followed_by_quote(modified_string):
            #     modified_string = modified_string.replace(
            #         " ", "").replace(',"year"', "")
            json_object = json.loads(modified_string)
            print(json_object)
            current_festivals.append({
                'name': obj['name'],
                'start': json_object['start'],
                'end': json_object['end'],
            })
        except Exception as e:
            print(e)
            print('\n')

with open('festival_with_tuned_time_2.json', 'w', encoding='utf-8') as file:
    json.dump(current_festivals, file, ensure_ascii=False)
