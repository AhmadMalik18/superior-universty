from flask import Flask, jsonify, request, render_template
from joke_api import get_joke
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/get-joke")
def joke():
    joke = get_joke()
    return jsonify(joke)
if __name__ == "__main__":
    app.run(debug=True)
