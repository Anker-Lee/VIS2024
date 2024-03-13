import json, nltk
import datetime

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Read the text file
with open('/Users/anker/Viseer/system/VIS2024/codes/document/LittleRedRidingHood.txt', 'r') as file:
    text = file.read()

# Split the text into sentences
sentences = sent_tokenize(text)

# Print the array of sentences
print(sentences)

# Store the sentence array in JSON format
json_data = json.dumps(sentences)

# Generate the current timestamp with minute precision
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")

# Construct the file name with the timestamp suffix
file_name_txt = f"./document/story_array_{timestamp}.txt"
file_name_json = f"./document/story_array_{timestamp}.json"


# Write the JSON data to the file with the timestamped name
with open(file_name_txt, 'w') as file:
    file.write(json_data)

with open(file_name_json, 'w') as file:
    file.write(json_data)