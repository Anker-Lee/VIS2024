from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# 你的 OpenAI API 密钥
OPENAI_API_KEY = 'sk-K8Wh5Gyq5eIqmGe2DaE07c5eDeB54fBd9eBcB427E0547e59'

# 配置 OpenAI 库使用你的 API 密钥
openai.api_key = OPENAI_API_KEY
openai.api_base = "https://ai-yyds.com/v1"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)