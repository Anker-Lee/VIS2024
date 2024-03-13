"""
此方法不可行
"""

import openai
import uuid

# 将YOUR_API_KEY替换为您的OpenAI API密钥
openai.api_key = "sk-K8Wh5Gyq5eIqmGe2DaE07c5eDeB54fBd9eBcB427E0547e59"
openai.api_base = "https://ai-yyds.com/v1"

# 生成一个唯一的对话ID
conversation_id = str(uuid.uuid4())

print(conversation_id)

# def chat_with_gpt(prompt):
#     """
#     使用conversation_id与GPT模型进行多轮对话。
#     :param prompt: 用户输入的文本
#     :return: 模型的响应文本
#     """
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # 指定模型
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         conversation_id=conversation_id  # 使用conversation_id维持对话上下文
#     )
    
#     # 从响应中获取模型的回复
#     model_response = response.choices[0].message['content']
#     return model_response

# # 循环接受用户输入，直到用户输入特定命令来结束对话
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ['quit', 'exit']:
#         print("Exiting the chat...")
#         break  # 用户输入终止命令时，退出循环
    
#     response = chat_with_gpt(user_input)
#     print("GPT:", response)
