import os
import json


def process_json_files(folder_path):
    """Read JSON files from a folder, extract the 'Sheet1' content, and save it back."""
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

            # Extract the content of "Sheet1" if it exists and is a list
            sheet_content = data.get("Sheet1", [])

            # Save only the "Sheet1" content back to the JSON file
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(sheet_content, file, ensure_ascii=False, indent=4)
                print(f"Processed and saved: {filename}")


# Specify the folder path containing JSON files
folder_path = 'json_data'

# Process all JSON files in the folder
process_json_files(folder_path)
