from handler.chatgpt_selenium_automation import ChatGPTAutomation
import json
import re
from itertools import dropwhile


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


file_path = 'refinedFestivalFromLehoiInfo_2.json'
json_objects = read_json_objects_from_file(file_path)

festivals = []
start_iteration = False

# Define the path where the chrome driver is installed on your computer
chrome_driver_path = r"F:\Downloads\chromedriver-win64\chromedriver.exe"

# the syntax r'"..."' is required because the space in "Program Files"
# in my chrome_path
chrome_path = r'"F:\Downloads\chrome-win64\chrome.exe"'

# Create an instance
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

# Define a prompt and send it to chatGPT
for obj in json_objects:
    if 'description' not in obj:
        continue
    if obj['name'] == "Lễ cúng Miễu tại Vĩnh Long":
        start_iteration = True
    if start_iteration:
        try:
            print(obj['name'])
            description = obj['description']
            # Retrieve the last response from chatGPT
            prompt = "Lễ hội có mô tả như sau có thờ nhân vật lịch sử nào trong phần mô tả dưới đây(không có hãy trả về null, không được bịa thông tin) ?" + description.replace(
                "'", " ") + "Hãy trả lời dưới dạng 1 json object ví dụ: {thờ: (tên 1 nhân vật lịch sử nào đó)}" + "Bạn không cần phải giải thích 1 điều gì chỉ cần trả về 1 json object là được, 1 lễ hội có thể thờ nhiều nhân vật lịch sử"
            chatgpt.send_prompt_to_chatgpt(prompt)
            response = chatgpt.return_last_response()
            print(response)
            json_string = response[response.index('{'):response.rindex('}')+1]
            modified_string = json_string.replace("'", '"').replace(
                "'", "\'").replace("ChatGPT\n", "")
            print(modified_string)
            json_object = json.loads(modified_string)
            print(json_object)
            festivals.append({
                'name': obj['name'],
                'thờ': json_object['thờ']
            })
        except Exception as e:
            print(e)
            print('\n')

with open('festival_historical_figure/extracted_using_chatgpt_31.json', 'w', encoding='utf-8') as file:
    json.dump(festivals, file, ensure_ascii=False)
