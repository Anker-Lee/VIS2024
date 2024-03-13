import json

def count_words(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    word_count = 0
    word_count_pure = 0 // 只考虑content中的内容
    OTHER_INFO_COUNT = 3 // 其他信息长度
    
    for scene in data:
        for conversation_action in scene['conversations_actions']:
            content = conversation_action['content']
            words = content.split()
            print(words)
            word_count = word_count + len(words) + OTHER_INFO_COUNT
            word_count_pure += len(words)
            print(word_count,word_count_pure)

    return word_count

file_path = '/Users/anker/Viseer/system/VIS2024/test_codes/data/processed_data_plup_fiction.json'
word_count = count_words(file_path)
print('Word count:', word_count)
