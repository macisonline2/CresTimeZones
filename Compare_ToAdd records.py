import pandas as pd


# Load the JSON file
json_data = pd.read_json('old_SiteTimeZones.json')  # Replace 'data.json' with your file name
# Convert to CSV
json_data.to_csv('old_SiteTimeZones.csv', index=False)  # Saves as 'data.csv'

print("JSON file has been converted to CSV.")

# Load the CSV files
new_df = pd.read_csv('new_SitesTimeZones.csv')
old_df = pd.read_csv('old_SiteTimeZones.csv')

# Identify records in new.csv whose Site_name is not in old.csv
missing_records = new_df[~new_df['SiteName'].isin(old_df['SiteName'])]

# Append missing records to old.csv
updated_old_df = pd.concat([old_df, missing_records])

# Save the updated old.csv
updated_old_df.to_csv('old_SiteTimeZones.csv', index=False)