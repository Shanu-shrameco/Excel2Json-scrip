import os
import json


def remove_empty_fields(data):
    if isinstance(data, dict):
        return {k: remove_empty_fields(v) for k, v in data.items() if v not in [None, "", [], {}]}
    elif isinstance(data, list):
        return [remove_empty_fields(item) for item in data]
    else:
        return data


def process_json_files(folder_path):
    """Read JSON files from a folder, remove empty fields, and save cleaned data."""
    # Iterate over all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)

            # Read the JSON file
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    print(f"Failed to decode {filename}. Skipping this file.")
                    continue

            # Clean the JSON data by removing empty fields
            cleaned_data = remove_empty_fields(data)

            # Save the cleaned JSON data back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(cleaned_data, file, ensure_ascii=False, indent=4)
                print(f"Cleaned and saved: {filename}")


# Specify the folder path containing JSON files
folder_path = 'json_data'

# Process all JSON files in the folder
process_json_files(folder_path)
