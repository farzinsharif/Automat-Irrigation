from flask import Flask, url_for, render_template
import json
import threading
import time
from datetime import date , datetime
import calendar


app = Flask(__name__)

output_path = '../Data/parsed_humidity_data.json'  # Adjust the path as needed
posts = []
last_read_time = ""
time_to_change = ""

def reader():
    global posts
    while True:
        try:

            with open(output_path, 'r') as json_file:
                posts = json.load(json_file)
            last_read_time = datetime.now().strftime('%d %B')  # Format as '15 July'
            time_to_change = datetime.now().strftime('%H:%M')
        except Exception as e:
            print(f"Error reading JSON file: {e}")
        time.sleep(6)  # Sleep for 30 seconds before reading again

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/showme")
def showme():
    return render_template('showme.html', posts=posts, last_read_time=last_read_time, time_to_change=time_to_change)

if __name__ == "__main__":
    # Start the background thread to read the JSON file continuously
    reader_thread = threading.Thread(target=reader)
    reader_thread.daemon = True
    reader_thread.start()

    app.run(debug=True)


