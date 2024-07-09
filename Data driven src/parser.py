import pandas as pd
from collections import defaultdict
from datetime import datetime
import json

# Load the data from the uploaded CSV file
file_path = '../Data/humidity_data.csv'
data = pd.read_csv(file_path, header=None, names=['moisture_level', 'timestamp'], skiprows=1)

# Dictionary to store grouped data by date
grouped_data = defaultdict(list)

# Parse each row and group by date
for index, row in data.iterrows():
    moisture_level = str(row['moisture_level'])
    timestamp = row['timestamp']
    try:
        timestamp_dt = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y')
    except ValueError as e:
        print(f"Error parsing timestamp: {e}")
        continue

    date_str = timestamp_dt.strftime('%d %B')  # Format date as '15 July'
    time_str = timestamp_dt.strftime('%H:%M:%S')  # Format time as '15:30'

    grouped_data[date_str].append({
        'time': time_str,
        'moisture_level': moisture_level
    })

# Convert the grouped data into the desired structure
result = [{'date': date, 'entries': entries} for date, entries in grouped_data.items()]

# Save the result to a JSON file
output_path = '../Data/parsed_humidity_data.json'
with open(output_path, 'w') as json_file:
    json.dump(result, json_file, indent=4)

print(f"Parsed data saved to: {output_path}")
