# Creates a Virtual Python Environment
# python3 -m venv .venv

# python3 -m pip install flask
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
