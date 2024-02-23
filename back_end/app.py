from flask_cors import CORS
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = 'sk-K8Wh5Gyq5eIqmGe2DaE07c5eDeB54fBd9eBcB427E0547e59'

# 配置 OpenAI 库使用你的 API 密钥
openai.api_key = OPENAI_API_KEY
openai.api_base = "https://ai-yyds.com/v1"

# 初始化对话历史记录
# 注意：这种方式仅适用于单用户且每次重启服务时会重置历史记录
# 在生产环境中，你可能需要一个更稳定的解决方案来存储对话历史，如数据库
chat_history = []

@app.route('/test', methods=['POST'])
def test_backend():
    user_message = request.json.get('message')

    # 将用户的消息添加到历史记录
    chat_history.append({"role": "user", "content": user_message})

    # 调用 OpenAI API 并传入完整的对话历史
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )

    # 从 API 响应中提取 ChatGPT 的回复并添加到历史记录
    gpt_response = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": gpt_response})

    # 返回 ChatGPT 的回复
    return jsonify({"message": gpt_response})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
