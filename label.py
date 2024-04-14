from handler.chatgpt_selenium_automation import ChatGPTAutomation
import json
from itertools import dropwhile


def read_json_objects_from_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


file_path = 'reviews/ShopeeReviews_1.json'
json_objects = read_json_objects_from_file(file_path)

reviews = []

chrome_driver_path = r"F:\Downloads\chromedriver-win64\chromedriver.exe"

chrome_path = r'"F:\Downloads\chrome-win64\chrome.exe"'

chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

for obj in json_objects:
    if 'comment' not in obj:
        continue
    try:
        print(obj['comment'])
        description = obj['comment']
        # Retrieve the last response from chatGPT
        prompt = "Comment dưới đây thể hiện neutral, positive hay negative đối với sản phẩm(neutral = 0, positive = 1, negative = 2). Comment:" + description.replace(
            "'", " ").replace("\n","") + "Hãy trả lời dưới dạng 1 json object ví dụ: {label: 0}" + "  Lưu ý: không cần phải giải thích 1 điều gì chỉ cần trả về 1 json object là được, 1 comment chỉ có thể là 1 trong 3 loại neutral, positive, negative"
        chatgpt.send_prompt_to_chatgpt(prompt)
        response = chatgpt.return_last_response()
        print(response)
        json_string = response[response.index('{'):response.rindex('}')+1]
        modified_string = json_string.replace("'", '"').replace(
            "'", "\'").replace("ChatGPT\n", "")
        print(modified_string)
        json_object = json.loads(modified_string)
        print(json_object)
        reviews.append({
            'rating': obj['rating'],
            'comment': obj['comment'],
            'label': json_object['label']
        })
    except Exception as e:
        print(e)
        print('\n')

with open('labeled_reviews/labeled_using_chatgpt_1.json', 'w', encoding='utf-8') as file:
    json.dump(reviews, file, ensure_ascii=False)
