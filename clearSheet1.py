import os
import json


def process_json_files(folder_path):
    """Read JSON files from a folder, extract the 'Responses' content, and save it back."""
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

            # Ensure data is a dictionary before trying to access 'Responses'
            if isinstance(data, dict) and "Responses" in data:
                # Extract the content of "Responses" if it exists and is a list
                sheet_content = data["Responses"]
            else:
                print(f"'Responses' not found or data is not a dictionary in {filename}. Skipping.")
                continue

            # Save only the "Responses" content back to the JSON file
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(sheet_content, file, ensure_ascii=False, indent=4)
                print(f"Processed and saved: {filename}")


# Specify the folder path containing JSON files
folder_path = 'c'

# Process all JSON files in the folder
process_json_files(folder_path)
