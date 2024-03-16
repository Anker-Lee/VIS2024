import json

def process_emoji():
    emojis = []
    while True:
        emoji = input("Enter an emoji (or 'q' to quit): ")
        if emoji == 'q':
            break
        emojis.append(emoji)

    with open('./document/emojis.json', 'w') as file:
        json.dump(emojis, file, ensure_ascii=False)

process_emoji()