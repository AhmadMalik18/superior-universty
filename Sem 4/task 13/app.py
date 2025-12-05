from flask import Flask, render_template, request, jsonify
from chat_model import init_model, get_response
app = Flask(__name__)
init_model()
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"response": "Invalid request. Please send a message."}), 400
        user_msg = data["message"].strip()
        if user_msg == "":
            return jsonify({"response": "Please enter a message."})
        bot_reply = get_response(user_msg)
        return jsonify({"response": bot_reply})
    except Exception as e:
        print("Error in /chat route:", e)
        return jsonify({"response": "Something went wrong. Please try again."}), 500
if __name__ == "__main__":
    app.run(debug=True)
