from flask_cors import CORS
import openai
from flask import Flask, request, jsonify
import json, nltk
import datetime
import os

nltk.download('punkt')
from nltk.tokenize import sent_tokenize     # Split the text into sentences

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = 'sk-SNChZMqoNU6IRKNX5e3084317e9549118c988063C3591a77'

# 用于存储对话历史的列表
chat_history = []

def chatgpt_request(key, messages):
    openai.api_key = os.getenv('OPENAI_KEY', default=key)
    openai.api_base = "https://ai-yyds.com/v1"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model = 'gpt-4-1106-preview',
        # model = 'gpt-4',
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message.content

def split_story_into_sentences(story):
    """
    对整个故事操作
    """
    print(story)
    if not isinstance(story, str):
        raise ValueError("Story must be a string")
    sentences_array = sent_tokenize(story)
    json_sentences = json.dumps(sentences_array)
    # Python 的 json.dumps() 函数来将一个数组（在 Python 中称为列表）转换为字符串。这个函数会将 Python 对象转换为 JSON 字符串。
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
    file_name_txt = f"./document/story_array_{timestamp}.txt"
    file_name_json = f"./document/story_array_{timestamp}.json"

    with open(file_name_txt, 'w') as file:
        file.write(json_sentences)

    with open(file_name_json, 'w') as file:
        file.write(json_sentences)

    return json_sentences, sentences_array

def split_story_into_scenes(sentence_list_of_story):
    """
    传入句子列表
    通过ChatGPT API分割场景, 返回场景开头和结尾的index
    """
    messages = [
        {"role": "system", "content": 
         """
        # Task
        Given an list of sentences splitted from a story, your task is to analyze the content of these sentences to understand the storyline and its progression. Pay close attention to any changes in setting or location transitions depicted in the narrative. Your goal is to divide the story into scenes based on these changes in setting. These scenes will be used to create the storyboard. Since only one scene can be depicted in a storyboard, each time the location changes it is judged to be the end of this scene.

        For each identified scene, you will provide details in JSON format. The format should include an array of objects, each representing a scene. Each object must contain three key-value pairs: 'id', 'begin_index', and 'end_index'. The 'id' should be a unique identifier for each scene, starting from 0 and incrementing by 1 for each subsequent scene. The 'begin_index' and 'end_index' should indicate the starting and ending sentence indexes of the scene within the original sentences array, respectively.

        You need to scene the story all the way through. Make sure the "end_index" of the last scene is the "index" of the last sentence in the story array.

        ----
        # Output Example
        ```
        [
        {"id": 0, "begin_index": 0, "end_index": 5},
        {"id": 1, "begin_index": 6, "end_index": 12},
        ...
        ]
        ```
        """}, 
        {"role": "user", "content": sentence_list_of_story}]
    
    chat_answer = chatgpt_request(OPENAI_API_KEY, messages)

    json_content = chat_answer.strip('```json\n').strip('\n```') # Remove the code block markdown
    scene_locate_info = json.loads(json_content) # Convert the JSON string to a list of dictionaries
    return scene_locate_info

def generate_scene_files(sentence_list_of_story, scene_locate_info):
    scene_list = [] # 用于存储场景信息
    for i, locate_info in enumerate(scene_locate_info):
        # print("locate_info:")
        # print(locate_info)
        start_index = locate_info['begin_index']
        end_index = locate_info['end_index']

        # Concatenate the sentences for the current scene
        scene_text = ' '.join(sentence_list_of_story[start_index:end_index+1])
        # print("scene_text:", i, scene_text)
        scene_list.append(scene_text)

        # Output the scene to a text file
        with open(f'./document/scene_{i+1}.txt', 'w') as f:
            f.write(scene_text)

    # Check if there are remaining sentences after the last scene
    if scene_locate_info[-1]['end_index'] < len(sentence_list_of_story) - 1:
        remaining_text = ' '.join(sentence_list_of_story[scene_locate_info[-1]['end_index']+1:])
        scene_list.append(remaining_text)
        with open(f'scene_{len(scene_locate_info)+1}.txt', 'w') as f:
            f.write(remaining_text)

    return scene_list

def get_scene_info(scene):
    """
    对单个场景操作
    """
    if not isinstance(scene, str):
        raise ValueError("Scene must be a string")
    
    messages = [{"role": "system", "content": """
        #Background#

        Extract information based on the scene text of a story. The generated information will be used for the computer to automatically generate a storyboard, hence it needs to accurately describe the contents of each scene.

        ----
        #Tasks#

        Task 1: Extract the following necessary information:
            1.1 "Character": The names of the character appearing in the scene, for example: "character": ["grandmother", "Little Red Riding Hood", "mother"]
            1.2 "Object": Objects that interact with the characters. Note: Do not consider objects that do not interact with the characters, such as objects in the background. For example: "object": ["a cap made of red velvet"]
            1.3 "Dialogue or Thought": List the characters' dialogues or thought processes in chronological order within the scene. If there are no dialogues and thought processes in a scene, then output an empty array. For example: "line": [{"name": "mother", "content": "Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother.", "type": "speak"}, {"name": "mother", "content": "I hope Little Red Riding Hood gets there safely.", "type": "thought"}]
            1.4 "Character Actions": List the characters' actions in chronological order within the scene. It is not necessary to match the original text exactly. Note: Focus on physical actions (e.g., "give"), not mental actions (e.g., "want to"). For example: "action": ["grandmother gave Little Red Riding Hood a little cap made of red velvet"]
            1.5 "SVO": Extract the key actions in the form of subject, verb, and object. For example: "svo": [{"subject": "grandmother", "verb": "gave", "object": "a little cap made of red velvet"}]. Note that if the character says more than one sentence at a time, you need to use several SVO objects to represent it. For example, One day her mother said to her: "Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother." should be represented as "svo": [{"subject": "mother", "verb": "said", "object": "Come Little Red Riding Hood."}, {"subject": "mother", "verb": "said", "object": "Here is a piece of cake and a bottle of wine. Take them to your grandmother."}, ...]
        Task 2: Use HTML <span></span> tags to mark the information extracted in Task 1 within the original text, differentiating them with the class attribute. Note: "Character", "Object", and "Character Actions" appearing in "Dialogue or Thought" do not need marking; Objects and characters that appear in "Character Actions" require nested marking. "Character": <span class="marked character"></span>; "Object": <span class="marked object"></span>; "Dialogue or Thought": <span class="marked line"></span>; "Character Actions": <span class="marked action"></span>. For example: "text": "Once upon a time there was a sweet little girl. Everyone who saw her liked her, but most of all her <span class="marked character">grandmother</span>, who did not know what to give the child next. Once she <span class="marked action">gave her a <span class="marked object">little cap made of red velvet</span></span>. Because it suited her so well, and she wanted to wear it all the time, she came to be known as <span class="marked character">Little Red Riding Hood</span>. One day her <span class="marked name">mother</span> said to her: <span class="marked line">\"Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother.\"</span> <span class="marked character">Mother</span> thought: <span class="marked line">\"I hope Little Red Riding Hood gets there safely.\"</span>"

        ----
        #Output#

        Based on the example below, output the results in JSON format.
        ```
        {
            "character": ["grandmother", "Little Red Riding Hood", "mother"],
            "object": ["a cap made of red velvet", ...],
            "line": [{"name": "mother", "content": "Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother.", "type": "speak"}, {"name": "mother", "content": "I hope Little Red Riding Hood gets there safely.", "type": "thought"}] // If there are no dialogues and thoughts, then "line": []
            "action": ["grandmother gave Little Red Riding Hood a little cap made of red velvet", ...],
            "svo": [{"subject": "grandmother", "verb": "gave", "object": "a little cap made of red velvet"}, {"subject": "mother", "verb": "said", "object": "Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother."}, ...],
            "text": "Once upon a time there was a sweet little girl. Everyone who saw her liked her, but most of all her <span class="marked character">grandmother</span>, who did not know what to give the child next. Once she <span class="marked action">gave her a <span class="marked object">little cap made of red velvet</span></span>. Because it suited her so well, and she wanted to wear it all the time, she came to be known as <span class="marked character">Little Red Riding Hood</span>. One day her <span class="marked name">mother</span> said to her: <span class="marked line">\"Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother.\"</span> <span class="marked character">Mother</span> thought: <span class="marked line">\"I hope Little Red Riding Hood gets there safely.\"</span>"
        }
        ```
        """}, 
        {"role": "user", "content": scene}]
    
    answer= chatgpt_request(OPENAI_API_KEY, messages)
    json_content = answer.strip('```json\n').strip('\n```') # Remove the code block markdown
    scene_info = json.loads(json_content) # Convert the JSON string to a list of dictionaries
    return scene_info

@app.route('/generate_story_info', methods=['POST'])
def generate_story_info():

    # IS_TEST = False
    IS_TEST = True

    if IS_TEST:
         # 读取story_info.json文件
        with open('./document/story_info.json', 'r') as f:
            story_info = json.load(f)
            print("=============================================")
            print("story_info:", story_info)
            print("=============================================")
    else:   
        story = request.json.get('message')

        sentence_list_of_story, sentence_array = split_story_into_sentences(story) # 前者为txt形式的array, 后者为list形式的array
        print("=============================================")
        print("sentence_list_of_story:", sentence_list_of_story)
        print("=============================================")
        scene_locate_info = split_story_into_scenes(sentence_list_of_story) # json格式的场景定位信息
        print("scene_locate_info:", scene_locate_info)
        print("=============================================")
        scene_list = generate_scene_files(sentence_array, scene_locate_info) # 场景列表
        print("scene_list:", scene_list)
        print("=============================================")

        story_info = []
        for i, scene in enumerate(scene_list):
            scene_info = get_scene_info(scene)
            print("scene_info:", i+1, " of ", len(scene_list), scene_info)
            print("=============================================")
            story_info.append(scene_info)
        print("story_info:", story_info)
        print("=============================================")

        # 保存story_info到本地
        with open('./document/story_info.json', 'w') as f:
            json.dump(story_info, f)

    # 返回生成的故事信息
    return jsonify({"message": story_info})



if __name__ == '__main__':
    app.run(debug=True, port=8080)
