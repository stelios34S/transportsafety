import pandas as pd

# File paths for all datasets
files = {
    'national_road_traffic_performance': 'Data/traffic/national road traffic performance by type of vehicle and type of road.xlsx'
}

# Assuming `files` is a dictionary of your file paths and you've already loaded the Excel sheets
dfs = {}  # To hold the DataFrames for each Excel file

for key, file in files.items():
    # Read each sheet in the Excel file and store the DataFrame
    dfs[key] = pd.read_excel(file, sheet_name=None)

# Initialize an empty list to store the rows
data_rows = []

# Define the columns (years 2000-2022 plus 'Country' as the first column)
years = list(range(2013, 2023))
columns = ['Year'] + years

#test_row = pd.Series(dfs['national_road_traffic_performance']['Sheet 2'].iloc[29].dropna()[1:].values, index=years)
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
#TOTAL
extract_row(dfs['national_road_traffic_performance']['Sheet 2'], 29, "Motorways")
extract_row(dfs['national_road_traffic_performance']['Sheet 3'], 29, "Urban Roads")
extract_row(dfs['national_road_traffic_performance']['Sheet 4'], 29, "Rural Roads")
extract_row(dfs['national_road_traffic_performance']['Sheet 5'], 29, "Other Roads")

# Create a DataFrame from the collected rows
final_df = pd.DataFrame(data_rows, columns=columns)

total_row = final_df.iloc[:, 1:].sum(axis=0)  # sum all columns except the first one (e.g., the 'Year' column)

# Create a new row with the totals and label it 'Total'
total_row = pd.DataFrame([['Total'] + total_row.tolist()], columns=final_df.columns)

# Append the 'Total' row to the original DataFrame
df_with_total = pd.concat([final_df, total_row], ignore_index=True)

# Optional: Print the new DataFrame with the total row
print(df_with_total)
df_with_total.to_csv('Data/clean_csv/road_performance_type.csv', index=False)
