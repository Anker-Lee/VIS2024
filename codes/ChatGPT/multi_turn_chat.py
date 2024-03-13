import openai

openai.api_key = "sk-K8Wh5Gyq5eIqmGe2DaE07c5eDeB54fBd9eBcB427E0547e59"
openai.api_base = "https://ai-yyds.com/v1"

def chat_with_gpt(prompt, chat_log=None):
    """
    与GPT模型进行多轮对话的函数。
    :param prompt: 用户输入的文本
    :param chat_log: 到目前为止的对话历史，用于保持对话上下文
    :return: 模型的响应文本和更新后的对话历史
    """
    if chat_log is None:
        chat_log = []  # 如果没有提供对话历史，就初始化一个空列表
    
    # 向对话历史中添加用户的输入
    chat_log.append({'role': 'user', 'content': prompt})
    
    # 使用OpenAI API进行请求
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 指定模型，这里使用的是gpt-3.5-turbo
        messages=chat_log  # 提供到目前为止的对话历史
    )
    
    # 从响应中获取模型的回复
    model_response = response['choices'][0]['message']['content']
    
    # 将模型的回复也添加到对话历史中
    chat_log.append({'role': 'assistant', 'content': model_response})
    
    return model_response, chat_log

# 初始化对话历史为空
chat_log = None

# 循环接受用户输入，直到用户输入特定命令来结束对话
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit']:
        print("Exiting the chat...")
        break  # 用户输入终止命令时，退出循环
    
    response, chat_log = chat_with_gpt(user_input, chat_log)
    print("GPT:", response)
