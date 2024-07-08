from flask import Flask, url_for, render_template
app = Flask(__name__)

posts = [
    {
        'date': '15 July',
        'entries': [
            {'time': '15:30', 'moisture_level': '1798'},
            {'time': '16:00', 'moisture_level': '1800'}
        ]
    },
    {
        'date': '22 March',
        'entries': [
            {'time': '23:47', 'moisture_level': '3215'},
            {'time': '00:00', 'moisture_level': '3220'},
            {'time': '15:30', 'moisture_level': '1798'},
            {'time': '16:00', 'moisture_level': '1800'}
        ]
    },
    {
        'date': '30 بهمن',
        'entries': [
            {'time': '23:47', 'moisture_level': '3215'},
            {'time': '00:00', 'moisture_level': '3220'}
        ]
    },
{
        'date': '1 august',
        'entries': [
            {'time': '23:47', 'moisture_level': '3215'},
            {'time': '00:00', 'moisture_level': '3220'}
        ]
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