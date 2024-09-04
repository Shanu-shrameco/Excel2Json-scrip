import os
import json


def trim_spaces(data):
    """
    Recursively trims whitespace from the start and end of keys and values in the data.
    Handles dictionaries and lists within the JSON data.
    """
    if isinstance(data, dict):
        # Create a new dictionary with trimmed keys and values
        return {k.strip(): trim_spaces(v) if isinstance(v, (dict, list)) else v.strip() if isinstance(v, str) else v
                for k, v in data.items()}
    elif isinstance(data, list):
        # Recursively clean each item in the list
        return [trim_spaces(item) for item in data]
    else:
        # Return data as is if it's not a list or dict
        return data


def process_json_files(folder_path):
    """Read JSON files from a folder, trim spaces from keys and values, and save the cleaned data."""
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

            # Ensure data is a list
            if isinstance(data, list):
                # Clean each JSON object inside the list
                cleaned_data = [trim_spaces(item) for item in data]

                # Save the cleaned data back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)
                    print(f"Processed and saved: {filename}")
            else:
                print(f"Unexpected format in {filename}. Expected a list at the root level.")


# Specify the folder path containing JSON files
folder_path = 'c'

# Process all JSON files in the folder
process_json_files(folder_path)
