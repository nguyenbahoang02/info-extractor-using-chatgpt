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
    if obj['name'] == "Hồ Tùng Mậu":
        start_iteration = True
    if start_iteration:
        try: 
            print(obj['name'])
            description = obj['description']
            # Retrieve the last response from chatGPT
            prompt = "Nhân vật có mô tả như sau có chức vụ gì ?" + description.replace("'"," ") +"Hãy trả lời dưới dạng 1 json object ví dụ: {chức vụ: Thượng tướng}" +"Bạn không cần phải giải thích 1 điều gì chỉ cần trả về 1 json object là được"
            chatgpt.send_prompt_to_chatgpt(prompt)
            response = chatgpt.return_last_response()
            print(response)
            pattern = r'\{[^{}]*\}'
            match = re.search(pattern, response)
            if match:
                json_string = match.group(0)
                modified_string = json_string.replace("'", '"').replace("'","\'").replace("ChatGPT\n","")
                json_object = json.loads(modified_string)
                historical_figures.append({
                    'name': obj['name'],                    
                    'chức vụ': json_object['chức vụ']
                })
        except Exception as e:
            print(e)
            print('\n')

with open('extracted_using_chatgpt_10.json', 'w', encoding='utf-8') as file:
    json.dump(historical_figures, file, ensure_ascii=False)