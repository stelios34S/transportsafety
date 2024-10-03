# This is a sample Python script.
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
    print(dfs)
    # You can access individual DataFrames like this:
    # dfs['motor_coaches_buses']['Sheet 1'] for example to access the 'Sheet 1' from the motor_coaches_buses dataset

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
