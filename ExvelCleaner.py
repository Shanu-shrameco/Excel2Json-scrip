import pandas as pd

# File paths
input_file = 'villages_files/Aldandi.xlsx'  # Replace with your actual input file path
format_file = 'format.xlsx'  # Replace with your format file path
output_file = 'separated_columns.xlsx'  # Name of the new file to save

# Read the input Excel file into a DataFrame
df = pd.read_excel(input_file)

# Read the format Excel file to get the header row
format_df = pd.read_excel(format_file, header=None)
new_header = format_df.iloc[0].tolist()  # Extract the first row as a list for headers

# Find the index of the column that includes "[Member 1]"
target_index = None
for idx, col in enumerate(df.columns):
    if "[Member 1]" in col:
        target_index = idx
        break

# Check if a column containing "[Member 1]" was found
if target_index is not None:
    # Select all columns before the identified column
    separated_df = df.iloc[:, :target_index]

    # Rename columns of the separated DataFrame using the format header row
    # Ensure the new header matches the number of columns in the separated data
    if len(new_header) >= len(separated_df.columns):
        separated_df.columns = new_header[:len(separated_df.columns)]
    else:
        print("Warning: The format file has fewer column headers than the separated data.")

    # Save the separated and renamed columns to a new Excel file
    separated_df.to_excel(output_file, index=False)
    print(f"Separated columns saved to {output_file} with updated headers.")
else:
    print("No column containing '[Member 1]' found in the file.")
