"""
生成场景中的信息
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
    with open('./document/scene_4.txt') as f:
        txt_data = f.read()
    story = json.dumps(txt_data) # Store the entire text as a single string in a list
    
    messages = [
        {"role": "system", "content": 
            """
# Task
Given a story fragment, we can create a corresponding storyboard by assembling emojis. In the storyboard, each character and item will have its own position information.
Task One: Based on the story fragment, deduce the scene content of the storyboard, and use this context to assign position information for each character and item in the scene. This information will be used to position these characters and items on a webpage, hence it is necessary for you to understand the story and deduce the exact positions of the emojis (with the center point of the emoji as the origin). The storyboard canvas is preset to 1600px * 900px, with the upper left corner as the origin (0,0) and the bottom right corner as (1600,900). Following the HTML element positioning standard, output the detailed positioning in JSON format.
Task Two: Provide the size multipliers for each character and item. Set the character size to 1 as the base size (i.e., 100px * 100px). Based on your understanding of the scene, set sizes according to the multipliers. For example, the cake could be 0.5, a tree could be 3.
Task Three: Task 3. Ensure that the elements in the final result do not overlap.

# Note
1. Only the positions of items that interact with the characters need to be given; items that may exist in the background do not need to be considered.
2. Only characters and items that physically appear in the scene need to be presented. Some characters and items may be mentioned in the text of the segment but do not appear in the corresponding scene. You need to ignore characters and items mentioned in background information or in characters' dialogues or thoughts. For example, in the segment "Once upon a time there was a sweet little girl. Everyone who saw her liked her, but most of all her grandmother, who did not know what to give the child next. Once she gave her a little cap made of red velvet. Because it suited her so well, and she wanted to wear it all the time, she came to be known as Little Red Riding Hood. One day her mother said to her: "Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother." The grandmother appears in this segment, but only as background information, not actually appearing in this scene.
3. Character and items are eventually rendered as an emoji. They are 100px * 100px when the multiplicity of the size is 1. So avoid overlapping each other in the layout.

# Output format, refer to the following example (the numerical values of the coordinates have no reference value and need to be set based on your overall layout)
```
[
{ "name": "Little Red Riding Hood", "x": 200, "y": 300, "size": 1},
{ "name": "mother", "x": 600, "y": 300, "size": 1},
{ "name": "cake", "x": 620, "y": 300, "size": 0.5},
{ "name": "wine", "x": 580, "y": 300, "size": 0.5},
{ "name": "red cap", "x": 200, "y": 250, "size": 0.5}"
]
```
"""}, 
        {"role": "user", "content": story}]
    
    text = chatgpt_request(KEY, messages)

    json_content = text.strip('```json\n').strip('\n```') # Remove the code block markdown

    final_data = json.loads(json_content) # Convert the JSON string to a list of dictionaries
    
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M")
    output_file = f"./document/element_location_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump(final_data, f, indent=4)
    print("finished")


if __name__ == "__main__":
    main()
