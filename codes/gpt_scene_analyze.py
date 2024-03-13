import requests
import openai
import os
import json
def generate_text(key, messages):
    openai.api_key = os.getenv('OPENAI_KEY', default=key)
    openai.api_base = "https://ai-yyds.com/v1"

    response = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model = 'gpt-4-1106-preview',
        messages=messages,
        temperature=1.0,
    )

    return response.choices[0].message.content


def main():
    with open('/Users/anker/Viseer/system/VIS2024/codes/document/LittleRedRidingHood.txt') as f:
        txt_data = f.read()
    story = json.dumps(txt_data)

    messages = [{"role": "system", "content": """
#Background#

Extract information based on the story text. The generated information will be used for the computer to automatically generate a storyboard, hence it needs to accurately describe the contents of each scene.

----
#Tasks#

Task 1: Divide the story text into different scenes based on the change of environment.
Task 2: For each scene, extract the following necessary information:
    2.1 "Character": The names of the character appearing in the scene, for example: "character": ["grandmother", "Little Red Riding Hood", "mother"]
	  2.2 "Object": Objects that interact with the characters. Note: Do not consider objects that do not interact with the characters, such as objects in the background. For example: "object": ["a cap made of red velvet"]
    2.3 "Dialogue or Thought": List the characters' dialogues or thought processes in chronological order within the scene. If there are no dialogues and thought processes in a scene, then output an empty array. For example: "line": [{"name": "mother", "content": "Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother.", "type": "speak"}, {"name": "mother", "content": "I hope Little Red Riding Hood gets there safely.", "type": "thought"}]
    2.4 "Character Actions": List the characters' actions in chronological order within the scene. It is not necessary to match the original text exactly. Note: Focus on physical actions (e.g., "give"), not mental actions (e.g., "want to"). For example: "action": ["grandmother gave Little Red Riding Hood a little cap made of red velvet"]
Task 3: Use HTML <span></span> tags to mark the information extracted in Task 2 within the original text, differentiating them with the class attribute. Note: "Character", "Object", and "Character Actions" appearing in "Dialogue or Thought" do not need marking; Objects and characters that appear in "Character Actions" require nested marking. "Character": <span class="marked character"></span>; "Object": <span class="marked object"></span>; "Dialogue or Thought": <span class="marked line"></span>; "Character Actions": <span class="marked action"></span>. For example: "text": "Once upon a time there was a sweet little girl. Everyone who saw her liked her, but most of all her <span class="marked character">grandmother</span>, who did not know what to give the child next. Once she <span class="marked action">gave her a <span class="marked object">little cap made of red velvet</span></span>. Because it suited her so well, and she wanted to wear it all the time, she came to be known as <span class="marked character">Little Red Riding Hood</span>. One day her <span class="marked name">mother</span> said to her: <span class="marked line">\"Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother.\"</span> <span class="marked character">Mother</span> thought: <span class="marked line">\"I hope Little Red Riding Hood gets there safely.\"</span>"

----
#Output#

Based on the example below, output the results in JSON format. Only 2 scences are provide for simplicity, you need to process and export all the scenes:
```
[ "scene": {
		"character": ["grandmother", "Little Red Riding Hood", "mother"],
		"object": ["a cap made of red velvet"],
		"line": [{"name": "mother", "content": "Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother.", "type": "speak"}, {"name": "mother", "content": "I hope Little Red Riding Hood gets there safely.", "type": "thought"}] // If there are no dialogues and thoughts, then "line": []
		"action": ["grandmother gave Little Red Riding Hood a little cap made of red velvet"],
		"text": "Once upon a time there was a sweet little girl. Everyone who saw her liked her, but most of all her <span class="marked character">grandmother</span>, who did not know what to give the child next. Once she <span class="marked action">gave her a <span class="marked object">little cap made of red velvet</span></span>. Because it suited her so well, and she wanted to wear it all the time, she came to be known as <span class="marked character">Little Red Riding Hood</span>. One day her <span class="marked name">mother</span> said to her: <span class="marked line">\"Come Little Red Riding Hood. Here is a piece of cake and a bottle of wine. Take them to your grandmother. She is sick and weak, and they will do her well. Mind your manners and give her my greetings. Behave yourself on the way, and do not leave the path, or you might fall down and break the glass, and then there will be nothing for your sick grandmother.\"</span> <span class="marked character">Mother</span> thought: <span class="marked line">\"I hope Little Red Riding Hood gets there safely.\"</span>"
		"id": 0
},
"scene": {
		"character": ["character 0", "character 1"],
		"object": ["object 0", "object 1"]
		"line": [{"name": "character 0", "content": "sentences", "type": "speak or thought"}, {"name": "character 1", "content": "sentences", "type": "speak or thought"}] // If there are no dialogues and thoughts, then "line": []
		"action": ["action 1", "action 2"],
		"text": "the tagged text of this scene"
		"id": 1
},
// Subsequent scenes omitted for simplicity in this example. You need to process and export all the scenes. 
]
```
"""}, 
        {"role": "user", "content": story}]
    
    text = generate_text("sk-SNChZMqoNU6IRKNX5e3084317e9549118c988063C3591a77", messages)
    
    with open('LittleRedRidingHood 0308 1951.txt', 'w') as f:
        f.write(text)

    print("finished")

if __name__ == "__main__":
    main()
