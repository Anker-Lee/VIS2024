"""
将故事分成不同的场景
"""

import openai
import os
import json
import json
import datetime

KEY = "sk-SNChZMqoNU6IRKNX5e3084317e9549118c988063C3591a77"

def chatgpt_request(key, messages):
    openai.api_key = os.getenv('OPENAI_KEY', default=key)
    openai.api_base = "https://ai-yyds.com/v1"

    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        # model = 'gpt-4-1106-preview',
        model = 'gpt-4',
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message.content


def main():
    with open('./document/test.txt') as f:
        txt_data = f.read()
    story = json.dumps(txt_data) # Store the entire text as a single string in a list
    
    messages = [
        {"role": "system", "content": 
         """
        # Task
        Given an array of sentences splitted from a story, your task is to analyze the content of these sentences to understand the storyline and its progression. Pay close attention to any changes in the environment, setting, or scene transitions depicted through the narrative. Your objective is to segment the story into distinct scenes based on these environmental shifts or significant narrative changes.

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
        {"role": "user", "content": story}]
    
    text = chatgpt_request(KEY, messages)

    json_content = text.strip('```json\n').strip('\n```') # Remove the code block markdown

    final_data = json.loads(json_content) # Convert the JSON string to a list of dictionaries
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M")
    output_file = f"./document/scene_location_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump(final_data, f, indent=4)
    print("finished")

    # test

    with open("./document/story_array_202403091044.json", 'r') as f:
        data_story = json.load(f)
        
    for d in final_data:
        print(d['id'], d['begin_index'], d['end_index'])
        print(data_story[d['begin_index']:d['end_index']]) # Print the sentences for each scene


if __name__ == "__main__":
    main()
