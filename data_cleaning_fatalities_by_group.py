import pandas as pd

# File path for the dataset
files = {
    'persons_killed_by_age_sex': 'Data/deaths/persons killed in road accidents by age, sex.xlsx',
}


dfs = {}

# Read each sheet in the Excel file and store them in the dfs dictionary
for key, file in files.items():
    dfs[key] = pd.read_excel(file, sheet_name=None)

year_dataframes = {}
combined_data = []

columns = ['Age group', 'Total fatalities', 'Fatalities per million', 'Male fatalities', 'Female fatalities']

age_groups = ['<15', '15-17', '18-24', '25-49', '50-64', '65>']

years = list(range(1999, 2023))
test_row = pd.Series(dfs['persons_killed_by_age_sex']['Sheet 1'].iloc[43].dropna()[1:].values, index=years)
print(test_row)

annual_data = {}

# Define the sheet numbers for each category
age_groups = [
    ('<15', 3, 4, 17, 31),
    ('15-17', 5, 6, 19, 33),
    ('18-24', 7, 8, 21, 35),
    ('25-49', 9, 10, 23, 37),
    ('50-64', 11, 12, 25, 39),
    ('65>', 13, 14, 27, 41),
    ('Total', 1, 2, 15, 29)  # Total gets values from Sheet 1
]

for year in years:
    # Create an empty DataFrame for the year
    annual_df = pd.DataFrame(columns=['Age Group', 'Fatalities', 'Per million inhabitants', 'Male', 'Female'])

    # Fill in the data for each age group
    for age_group, fatalities_sheet, per_million_sheet, male_sheet, female_sheet in age_groups:
        # Retrieve the corresponding row from the correct sheets
        fatalities_data = pd.Series(dfs['persons_killed_by_age_sex'][f'Sheet {fatalities_sheet}'].iloc[43].dropna()[1:].values, index=years)
        per_million_data = pd.Series(dfs['persons_killed_by_age_sex'][f'Sheet {per_million_sheet}'].iloc[43].dropna()[1:].values, index=years)
        male_data = pd.Series(dfs['persons_killed_by_age_sex'][f'Sheet {male_sheet}'].iloc[43].dropna()[1:].values, index=years)
        female_data = pd.Series(dfs['persons_killed_by_age_sex'][f'Sheet {female_sheet}'].iloc[43].dropna()[1:].values, index=years)

        # Create a new DataFrame row
        new_row = {
            'Age Group': age_group,
            'Fatalities': fatalities_data.loc[year],
            'Per million inhabitants': per_million_data.loc[year],
            'Male': male_data.loc[year],
            'Female': female_data.loc[year]
        }
        new_row_df = pd.DataFrame([new_row])
        # Append the new row to the DataFrame
        annual_df = pd.concat([annual_df, new_row_df], ignore_index=True)

    # Store the DataFrame for the year
    annual_data[year] = annual_df

print(annual_data[2019])

cut_years = list(range(1999, 2019))
for year in years:
    df_to_save = annual_data[year]
    df_to_save.to_csv(f'Data/clean_csv/{year}_fatality_group.csv', index=False)
