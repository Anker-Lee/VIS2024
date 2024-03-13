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
        {"role": "system", "content": """Completion of 12 analytical tasks using movie script data. A script is a list of scenes, each with the following attributes:
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


        Process the script data in this way to extract key events, characters and their interactions to summarize the plot of the entire movie. Make sure that the summarization follows the narrative order and clearly depicts the main lines and important turning points of the movie. 12 analytical tasks:
        1. Character Traits: "Analyze the character traits of the protagonist, Jules, in the screenplay, including his motivations, strengths and weaknesses, and how he changes as the story develops."
        2. Character Relationships: "Describe how the relationships between the main characters in the screenplay evolve over the course of the story. Pay special attention to their conflicts, how these conflicts are resolved, and the impact on the plot."
        3. Major Events: "Outline the major events and turning points in the screenplay, and how these events drive the story forward to its climax."
        4. Plot Structure: "Analyze the plot structure of the screenplay, identifying whether it follows a traditional three-act structure or uses nonlinear storytelling. Discuss how this structure affects the presentation of the story and the audience's experience."
        5. Theme Analysis: "Explore the core themes of the screenplay, such as love, revenge, or growth, and how the author demonstrates these themes through the story and characters."
        6. Symbols: "Identify any symbolic elements (such as objects, scenes, or characters) in the screenplay and their symbolic meanings, explaining how they deepen the understanding of the story's themes or characters."
        7. Dialogue Style: "Analyze the style of dialogue in the screenplay, including its characteristics (such as humorous, sarcastic, formal) and how this style serves to shape the characters and develop the story."
        8. Narrative Techniques: "Discuss the narrative perspective (such as first-person, omniscient) adopted in the screenplay, and analyze how this choice impacts the storytelling and audience comprehension."
        9. Emotional Fluctuations: "Analyze the fluctuations in emotion throughout the screenplay, identifying which scenes or events lead to emotional highs and lows, and the impact on the storyline."
        10. Scene Atmosphere: "Describe the atmosphere and emotional backdrop of specific scenes, for example, how the environment description, character actions, and dialogue contribute to creating a tense, relaxed, or sorrowful mood."
        11. Location and Time: "List several key scenes' locations and timing in the screenplay, explaining how these choices affect the story's setting and characters' actions."
        12. Scene Details: "Extract a detailed visual description of a specific scene, including environmental details and interactions between characters, and how these details contribute to the overall story's atmosphere and depth." 

        Your answer should follow the following form, and each answer is approximately 250 words long :
        1. Character Traits: Your answer...
        2. Character Relationships: Your answer...
        ... 
        12. Scene Details: Your answer..."""},
        {"role": "user", "content": json_string}
    ]
    text = generate_text("sk-SNChZMqoNU6IRKNX5e3084317e9549118c988063C3591a77", messages)
    
    with open('output_summarize.txt', 'w') as f:
        f.write(text)

if __name__ == "__main__":
    main()
