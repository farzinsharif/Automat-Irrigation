from flask import Flask, url_for, render_template
app = Flask(__name__)





@app.route("/")
def home():
    return render_template("index.html")

@app.route("/showme")
def data():
    with open("humidity-data.csv", "r") as file1:
        read_content = file1.readlines()
        return read_content



if __name__ == "__main__":
    app.run(debug=True)