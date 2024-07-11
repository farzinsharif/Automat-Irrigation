import schedule
import time
import pandas as pd
from collections import defaultdict
from datetime import datetime
import json
import os

def parse_and_save_data():
    # Load the data from the CSV file
    file_path = '../Data/humidity_data.csv'  # Change this to the actual path if needed
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
    new_data = [{'date': date, 'entries': entries} for date, entries in grouped_data.items()]

    # Load existing data from the JSON file
    output_path = '../Data/parsed_humidity_data.json'  # Change this to the desired output path
    if os.path.exists(output_path):
        with open(output_path, 'r') as json_file:
            existing_data = json.load(json_file)
    else:
        existing_data = []

    # Merge new data with existing data, avoiding duplicates
    date_to_entries = {entry['date']: entry['entries'] for entry in existing_data}
    for new_entry in new_data:
        date = new_entry['date']
        if date in date_to_entries:
            existing_times = {entry['time'] for entry in date_to_entries[date]}
            for entry in new_entry['entries']:
                if entry['time'] not in existing_times:
                    date_to_entries[date].append(entry)
        else:
            date_to_entries[date] = new_entry['entries']

    # Convert the merged data back to the required format
    merged_data = [{'date': date, 'entries': entries} for date, entries in date_to_entries.items()]

    # Save the updated data back to the JSON file
    with open(output_path, 'w') as json_file:
        json.dump(merged_data, json_file, indent=4)

    print(f"Parsed data saved to: {output_path}")

# Schedule the task every 30 minutes
schedule.every(5).seconds.do(parse_and_save_data)

# Run the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
