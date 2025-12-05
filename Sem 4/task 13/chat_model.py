import os
import json
import re
from random import choice
intents_path = os.path.join(os.path.dirname(__file__), "intents.json")
intents = {}
user_state = {}  
def clean(text):
    text = text.lower()
    text = re.sub(r'[^\w\s\d]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
def init_model():
    global intents
    if os.path.exists(intents_path):
        with open(intents_path, "r", encoding="utf-8") as f:
            intents.update(json.load(f))
        print("Travel chat assistant model loaded")
    else:
        intents.clear()
        print("No intents file found")
def keyboard_match(msg, pattern):
    return clean(pattern) in clean(msg)
def random_response(tag):
    for intent in intents.get("intents", []):
        if intent["tag"] == tag:
            return choice(intent.get("responses", ["Sorry, I didn't understand."]))
    return "Sorry, I didn't understand."
def handle_greeting(msg):
    return random_response("greeting")
def handle_how_are_you(msg):
    return random_response("how_are_you")
def handle_goodbye(msg):
    return random_response("goodbye")
def handle_thanks(msg):
    return random_response("thanks")
def handle_study_visa(msg):
    budget_match = re.search(r'(\d+)\s*m', msg)
    if budget_match:
        budget = int(budget_match.group(1))
        user_state["last_intent"] = "study_visa"
        if budget >= 20:
            return "With a budget above 20M, top options are: Lithuania, Romania, Poland."
        elif 10 <= budget < 20:
            return "With a budget of 10M–20M, Malaysia & Turkey are great study visa options."
        elif 5 <= budget < 10:
            return "With a budget of 5M–10M, Turkey and some affordable European countries are possible."
        else:
            return "Study visa below 5M is difficult. Minimum recommended is 5M."
    else:
        user_state["last_intent"] = "study_visa"
        return random_response("study_visa")
def handle_visit_visa(msg):
    stay_days = re.search(r'\b(\d+)\s*(day|days|month|months)\b', msg)
    user_state["last_intent"] = "visit_visa"
    if stay_days:
        number = stay_days.group(1)
        unit = stay_days.group(2)
        return f"Great! You want to stay for {number} {unit}. Please tell me your destination."
    return random_response("visit_visa")
def handle_umrah(msg):
    umrah_days = re.search(r'\b(8|15|21|28)\b', msg)
    user_state["last_intent"] = "umrah"
    if umrah_days:
        days = umrah_days.group(1)
        return f"Excellent! {days}-day Umrah package selected. Economy or premium?"
    return random_response("umrah")
def handle_hotel(msg):
    match = re.search(r'(\d+)\s*(day|days)', msg)
    if match:
        days = match.group(1)
        return f"Okay! You plan to stay for {days} days. Which city and hotel category (3, 4, 5 star)?"
    return random_response("hotel")
def handle_ticket(msg):
    countries = ["dubai", "turkey", "baku", "malaysia", "saudi arabia",
                 "germany", "france", "italy", "uk", "usa", "canada", "japan"]
    for country in countries:
        if country in msg:
            return f"Perfect! Starting ticket booking for {country.title()}."
    return random_response("flight_ticket")
def handle_package(msg):
    return random_response("tour_packages")
def get_response(user_msg):
    msg = clean(user_msg)
    last_intent = user_state.get("last_intent")
    if last_intent == "study_visa" and re.search(r'\d+\s*m', msg):
        return handle_study_visa(msg)
    if last_intent == "visit_visa" and re.search(r'\b(\d+)\s*(day|days|month|months)\b', msg):
        return handle_visit_visa(msg)
    if last_intent == "umrah" and re.search(r'\b(8|15|21|28)\b', msg):
        return handle_umrah(msg)
    if any(word in msg for word in ["hello", "hi", "salam", "hey", "assalamualaikum"]):
        return handle_greeting(msg)
    if any(word in msg for word in ["how are you", "how's it going", "what's up"]):
        return handle_how_are_you(msg)
    if any(word in msg for word in ["bye", "goodbye", "see you", "khuda hafiz"]):
        return handle_goodbye(msg)
    if any(word in msg for word in ["thanks", "thank you", "shukria"]):
        return handle_thanks(msg)
    if "study visa" in msg or "study" in msg:
        return handle_study_visa(msg)
    if "visit visa" in msg or "visit" in msg:
        return handle_visit_visa(msg)
    if "umrah" in msg:
        return handle_umrah(msg)
    if "hotel" in msg or "stay" in msg:
        return handle_hotel(msg)
    if any(word in msg for word in ["ticket", "flight", "airline", "fare"]):
        return handle_ticket(msg)
    if any(word in msg for word in ["package", "tour", "holiday"]):
        return handle_package(msg)
    for intent in intents.get("intents", []):
        for pattern in intent.get("patterns", []):
            if keyboard_match(msg, pattern):
                responses = intent.get("responses", [])
                if responses:
                    return choice(responses)
    return "Sorry, I didn't understand. You can ask about flights, visas, packages, hotels, or tickets."

if __name__ == "__main__":
    init_model()
    print("Travel Chat Assistant is ready. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a wonderful trip! ✈️")
            break
        print("Bot:", get_response(user_input))
