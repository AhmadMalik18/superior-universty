from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def get_reply(message):
    msg = message.lower()

    if "room" in msg:
        return "We offer Single, Double, Deluxe, and Suite rooms."
    elif "price" in msg or "cost" in msg:
        return "Prices: Single PKR 6000, Double PKR 9000, Deluxe PKR 12000, Suite PKR 20000."
    elif "amenities" in msg or "facility" in msg:
        return "Amenities include Free WiFi, Breakfast, Pool, Gym, and 24/7 Room Service."
    elif "book" in msg or "booking" in msg:
        return "To book a room, please share your name, dates, and room type."
    else:
        return "I can help with room types, prices, amenities, and booking details."
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.form.get("message")
    reply = get_reply(user_msg)
    return jsonify({"reply": reply})
if __name__ == "__main__":
    app.run(debug=True)
