# This is a sample Python script.
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

pd.set_option('display.max_rows', None)    # Show all rows
pd.set_option('display.max_columns', None) # Show all columns
pd.set_option('display.width', None)       # Ensure proper line wrapping
pd.set_option('display.max_colwidth', None) # No column width truncation
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # File paths for all datasets
    files = {
        'motor_coaches_buses': 'Data/numbers_of_cars_and_coaches/Motor coaches, buses and trolley buses by age.xlsx',
        'passenger_cars_per_thousand': 'Data/numbers_of_cars_and_coaches/Passenger cars - per thousand inhabitants.xlsx',
        'passenger_cars_by_age': 'Data/numbers_of_cars_and_coaches/Passenger cars by age.xlsx',
        'persons_killed_by_age_sex': 'Data/deaths/persons killed in road accidents by age, sex.xlsx',
        'persons_killed_by_type_road': 'Data/deaths/persons killed in road accidents by type of road.xlsx',
        'length_motorways_eroads': 'Data/road_types_and_length/length of motorways and e-roads.xlsx',
        'length_other_roads': 'Data/road_types_and_length/Length of other roads withinoutside built-up areas.xlsx',
        'length_paved_unpaved': 'Data/road_types_and_length/Length of paved and unpaved roads.xlsx',
        'length_state_provincial_communal': 'Data/road_types_and_length/Length of state, provincial and communal roads.xlsx',
        'total_length_motorways': 'Data/road_types_and_length/Total length of motorways.xlsx',
        'national_road_traffic_performance': 'Data/traffic/national road traffic performance by type of vehicle and type of road.xlsx'
    }

    # Dictionary to store all the dataframes
    dfs = {}

    # Loop over each file and read all sheets into separate DataFrames
    for key, file in files.items():
        # Read each sheet in the Excel file
        dfs[key] = pd.read_excel(file, sheet_name=None)
    #print((dfs['motor_coaches_buses']['Sheet 2']))
    print(dfs['persons_killed_by_type_road']['Sheet 1'])
    total_type_road = dfs['persons_killed_by_type_road']['Sheet 1']
    selected_row = total_type_road.iloc[41]
    selected_row = selected_row.dropna()
    print(selected_row)
    print(selected_row[1])
    idx = list(range(2000,2023))
    idx.insert(0, 'Country')
    print(idx)
    # Create a new DataFrame or Series with the cleaned data and assign the years as column labels
    cleaned_row_with_years = pd.Series(data=selected_row.values, index=idx)

    # Print the row with the new labels
    print(cleaned_row_with_years)

    # dfs['motor_coaches_buses']['Sheet 1'] for example to access the 'Sheet 1' from the motor_coaches_buses dataset

