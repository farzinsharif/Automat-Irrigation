from flask import Flask, url_for, render_template
app = Flask(__name__)

posts = [
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '22 march',
        'time': '23:47',
        'moisture_level': '3215'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
    {
        'date': '15 july',
        'time': '15:30',
        'moisture_level': '1798'

    },
]



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/showme")
def showme():
    return render_template('showme.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)