import json

def generate_scene_files(story_file, scene_file):
    # Load the JSON files
    with open(story_file, 'r') as f:
        story = json.load(f)
    with open(scene_file, 'r') as f:
        scenes = json.load(f)

    # Iterate over each scene
    for i, scene in enumerate(scenes):
        start_index = scene['begin_index']
        end_index = scene['end_index']

        # Concatenate the sentences for the current scene
        scene_text = ' '.join(story[start_index:end_index+1])

        # Output the scene to a text file
        with open(f'./document/scene_{i+1}.txt', 'w') as f:
            f.write(scene_text)

    # Check if there are remaining sentences after the last scene
    if scenes[-1]['end_index'] < len(story) - 1:
        remaining_text = ' '.join(story[scenes[-1]['end_index']+1:])
        with open(f'scene_{len(scenes)+1}.txt', 'w') as f:
            f.write(remaining_text)


def main():
    generate_scene_files('./document/story_array_202403091044.json', './document/scene_location_20240309_1056.json') 

if __name__ == "__main__":
    main()