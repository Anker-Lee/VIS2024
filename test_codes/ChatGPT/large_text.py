import requests
import openai
import os
import json
def generate_text(key, task, summary, snippet):
    openai.api_key = os.getenv('OPENAI_KEY', default=key)
    openai.api_base = "https://ai-yyds.com/v1"
    
    messages = [
        {"role": "system", "content": "You are a writer who specializes in rewriting. You will be provided with a \{story summary\} (separated by XML tags) and a \{story snippet\} wrapped in triple quotes." + task},
        {"role": "user", "content": """
         Story summary: <article>""" + summary + """</article>
         Story snippet: '''""" + snippet + """'''
        """}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.0,
    )

    return response.choices[0].message.content


def main():
    with open('document.json') as f:
        data = json.load(f)
    
    task = data['task']
    summary = data['summary']
    snippets = data['snippets']
    
    result = ""
    for snippet in snippets:
        text = generate_text("sk-K8Wh5Gyq5eIqmGe2DaE07c5eDeB54fBd9eBcB427E0547e59", task, summary, snippet)
        result += text + "\n"
    
    with open('output.txt', 'w') as f:
        f.write(result)

if __name__ == "__main__":
    main()
