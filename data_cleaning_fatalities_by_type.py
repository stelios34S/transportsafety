import pandas as pd

# File paths for all datasets
files = {
    'persons_killed_by_type_road': 'Data/deaths/persons killed in road accidents by type of road.xlsx',
}

# Assuming `files` is a dictionary of your file paths and you've already loaded the Excel sheets
dfs = {}  # To hold the DataFrames for each Excel file

for key, file in files.items():
    # Read each sheet in the Excel file and store the DataFrame
    dfs[key] = pd.read_excel(file, sheet_name=None)

# Initialize an empty list to store the rows
data_rows = []

# Define the columns (years 2000-2022 plus 'Country' as the first column)
years = list(range(2000, 2023))
columns = ['Year'] + years

# Function to extract row from a specific sheet and append it to data_rows
def extract_row(sheet, row_index, road_type):
    selected_row = sheet.iloc[row_index]  # Select the row
    print("Selected Row (Before Processing):", selected_row)  # Check before processing

    # Remove the first element (which is the index) and drop NaN values
    cleaned_row = selected_row[1:].dropna()  # Drop the first column (index) and NaNs
    print("Cleaned Row (After Removing First Element and NaNs):", cleaned_row)  # Check cleaned row

    # Ensure we are consistent with the number of columns
    if len(cleaned_row) + 1 == len(columns):  # +1 for the 'Country' key
        row_with_key = [road_type] + cleaned_row.tolist()  # Add road type as first value
        data_rows.append(row_with_key)  # Append the row to data_rows
    else:
        print(
            f"Warning: Row length mismatch for {road_type}: {len(cleaned_row)} values found, expected {len(columns) - 1}")


# Extract the relevant rows from each sheet:
# Assuming row 41 is the one containing fatality data for all types
extract_row(dfs['persons_killed_by_type_road']['Sheet 1'], 41, "Total")
extract_row(dfs['persons_killed_by_type_road']['Sheet 2'], 41, "Motorways")
extract_row(dfs['persons_killed_by_type_road']['Sheet 3'], 41, "Urban Roads")
extract_row(dfs['persons_killed_by_type_road']['Sheet 4'], 41, "Rural Roads")

# Create a DataFrame from the collected rows
final_df = pd.DataFrame(data_rows, columns=columns)
final_df.to_csv('Data/clean_csv/fatality_road_type.csv', index=False)
# Print the final DataFrame
print(final_df)