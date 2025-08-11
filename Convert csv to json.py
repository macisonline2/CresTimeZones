import pandas as pd


def convert_csv_to_json_pandas(csv_filepath, json_filepath):
    df = pd.read_csv(csv_filepath)

    # Convert specific column(s) to numeric, if needed
    # Replace 'your_numeric_column' with the actual column name
    df['your_numeric_column'] = pd.to_numeric(df['your_numeric_column'], errors='coerce')

    df.to_json(json_filepath, orient='records', indent=4)  # orient='records' for list of objects

# Example usage:
convert_csv_to_json_pandas('NewSiteTimeZones.csv', 'NewSiteTimeZones.json')
