import pandas as pd

# Load the Excel file
input_file = 'data.xlsx'  # Replace with your actual file path
output_file = 'separated_columns.xlsx'  # Name of the new file to save

# Read the Excel file into a DataFrame
df = pd.read_excel(input_file)

target_index = None
for idx, col in enumerate(df.columns):
    if "[Member 1]" in col:
        target_index = idx
        break

# Check if a column containing "[Member 1]" was found
if target_index is not None:
    # Select all columns before the identified column
    separated_df = df.iloc[:, :target_index]

    # Save the separated columns to a new Excel file
    separated_df.to_excel(output_file, index=False)
    print(f"Separated columns saved to {output_file}")
else:
    print("No column containing '[Member 1]' found in the file.")