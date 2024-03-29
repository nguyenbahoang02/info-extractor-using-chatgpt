from handler.chatgpt_selenium_automation import ChatGPTAutomation
import json
import re
from itertools import dropwhile

def read_json_objects_from_file(file_path):
    with open(file_path, 'r',encoding="utf8") as file:
        data = json.load(file)
    return data

file_path = 'HFFromWikipedia_2.json'
json_objects = read_json_objects_from_file(file_path)

historical_figures = []
start_iteration = False

# Define the path where the chrome driver is installed on your computer
chrome_driver_path = r"F:\Downloads\chromedriver-win64\chromedriver.exe"

# the sintax r'"..."' is required because the space in "Program Files" 
# in my chrome_path
chrome_path = r'"F:\Downloads\chrome-win64\chrome.exe"'

# Create an instance
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

# Define a prompt and send it to chatGPT
for obj in json_objects:
    if 'description' not in obj:
        continue
    if obj['name'] == "Ngô Thế Vinh":
        start_iteration = True
    if start_iteration:
        try: 
            print(obj['name'])
            description = obj['description']
            # Retrieve the last response from chatGPT
            prompt = "Nhân vật có mô tả như sau có liên hệ gì với các nhân vật trong phần mô tả dưới đây(chỉ cần quan hệ trong gia đình như cha con chị em không cần đồng nghiệp hay đối thủ, không có hãy trả về null, không được bịa thông tin) ?" + description.replace("'"," ") +"Hãy trả lời dưới dạng 1 json object ví dụ: {liên hệ: [{loại: cha,tên: Trần Quốc Toản},{loại:mẹ,{tên: trưng trắc}]}" +"Bạn không cần phải giải thích 1 điều gì chỉ cần trả về 1 json object là được, 1 số nhân vật có thể có nhiều liên hệ"
            chatgpt.send_prompt_to_chatgpt(prompt)
            response = chatgpt.return_last_response()
            print(response)
            json_string = response[response.index('{'):response.rindex('}')+1]
            modified_string = json_string.replace("'", '"').replace("'","\'").replace("ChatGPT\n","")
            print(modified_string)
            json_object = json.loads(modified_string)
            print(json_object)
            historical_figures.append({
                'name': obj['name'],                    
                'liên hệ': json_object['liên hệ']
            })
        except Exception as e:
            print(e)
            print('\n')

with open('relation/extracted_using_chatgpt_11.json', 'w', encoding='utf-8') as file:
    json.dump(historical_figures, file, ensure_ascii=False)