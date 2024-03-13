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
    # messages = [
    #     {"role": "system", "content": "You are a writer who specializes in rewriting. You will be provided with a \{story summary\} (separated by XML tags) and a \{story snippet\} wrapped in triple quotes." + task},
    #     {"role": "user", "content": """
    #      Story summary: <article>""" + summary + """</article>
    #      Story snippet: '''""" + snippet + """'''
    #     """}
    # ]

    """
    确保JSON数据是字符串格式: 因为你的messages列表中的content字段预期是一个字符串, 如果你想插入JSON数据, 你应该首先将其序列化成一个字符串。这可以通过json.dumps()函数实现。
    避免双引号冲突: 如果你的JSON字符串内部包含双引号, 直接插入时需要确保这些双引号不会打断Python字符串的边界。通常, 可以通过三引号来定义字符串, 或者使用转义字符\来避免冲突。
    使用json.dumps()处理JSON数据: 如果你有一个Python字典或列表, 并希望将其转换为JSON格式的字符串, 可以使用json.dumps()方法。
    """
    
    with open('/Users/anker/Viseer/system/VIS2024/test_codes/data/processed_data_plup_fiction_narrative_order.json') as f:
        json_data = json.load(f)
    json_string = json.dumps(json_data)

    messages = [
        {"role": "system", "content": """Please summarize the plot of a movie using movie script data (approximately 3000 words in length). A script is a list of scenes, each with the following attributes:
        - narrative_order: The order in which scene is presented in the story. 
        - story_order: The actual order of scene in story.
        - characters: List of characters appearing in the scene.
        - heading: Background information about the scene, such as time and place.
        - conversations_actions: A list of the dialog and action in the scene, including the content of the dialogue or action, the order in the scene, the type (type is the conversation or action), and the character who said the lines.

        Below is a sample script snippet to assist you in understanding data structures, using the first scene as an example:
        scenes = [
            {
                "narrative_order": 0, // This scene is 0th scene in the story presentation
                "characters": [ // List of characters in this scene
                    "Young Man",
                    "Young Woman"
                ],
                "story_order": 29, // This scene is the 29th event that actually happened
                "heading": "INT. COFFEE SHOP \u0096- MORNING", // Background information for this scene
                "conversations_actions": [ // List of dialog and actions in this scene
                    {
                        "content": "A normal Denny's, Spires-like coffee shop in Los Angeles.It's about 9:00 in the morning. While the place isn't jammed,there's a healthy number of people drinking coffee, munchingon bacon and eating eggs.Two of these people are a YOUNG MAN and a YOUNG WOMAN. TheYoung Man has a slight working-class English accent and,like his fellow countryman, smokes cigarettes like they'regoing out of style.It is impossible to tell where the Young Woman is from orhow old she is; everything she does contradicts somethingshe did. The boy and girl sit in a booth. Their dialogue isto be said in a rapid pace \"HIS GIRL FRIDAY\" fashion.", // Action content
                        "order": 0, // The 0th action or line that occurs in this scene
                        "type": "action", // Type is Action
                        "character": "" // character of type action is none.
                    },
                    {
                        "character": "Young Man", // Name of the character who said the line
                        "order": 1, // The 1st action or line that occurs in this scene 
                        "type": "conversation", // Type is conversation
                        "content": "No, forget it, it's too risky. I'mthrough doin' that shit." // Line content
                    },
                    ... // Subsequent actions or lines are omitted here
                ]
            },
            ... // The scene afterward is omitted here
        ]
        Process the script data in this way to extract key events, characters and their interactions to summarize the plot of the entire movie. Make sure that the summarization follows the narrative order and clearly depicts the main lines and important turning points of the movie. Please summarize the plot of a movie using movie script data (approximately 3000 words in length)."""},
        {"role": "user", "content": json_string}
    ]
    text = generate_text("sk-SNChZMqoNU6IRKNX5e3084317e9549118c988063C3591a77", messages)
    
    with open('output.txt', 'w') as f:
        f.write(text)

if __name__ == "__main__":
    main()
