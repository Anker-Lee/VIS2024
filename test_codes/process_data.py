import json

def process_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    scenes = data['script_info']['scenes']
    
    for scene in scenes:
        conversations = scene['conversations']
        actions = scene['actions']
        
        conversations_actions = conversations + actions
        conversations_actions.sort(key=lambda x: x['order'])
        
        for item in conversations_actions:
            item['type'] = 'conversation' if 'dialogue' in item else 'action'
            if 'dialogue' in item:
                all_sentence = ''
                for dialogue in item['dialogue']:
                    if dialogue['type'] == 'Dialogue':
                        all_sentence += dialogue['content']
                item['content'] = all_sentence
                del item['dialogue']
            if 'character' not in item:
                item['character'] = ''
        
        scene['conversations_actions'] = conversations_actions

        del scene['conversations']
        del scene['actions']
        del scene['character_metadata']
        del scene['scene_metadata']
    
    with open(output_file, 'w') as f:
        json.dump(scenes, f, indent=4)

# Example usage
input_file = '/Users/anker/Viseer/system/VIS2024/test_codes/pulp_fiction.json'
output_file = '/Users/anker/Viseer/system/VIS2024/test_codes/processed_data.json'
process_data(input_file, output_file)
