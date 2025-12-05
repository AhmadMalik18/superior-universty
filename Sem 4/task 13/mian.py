from chat_model import init_model, get_response

def main():
    init_model()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("quit", "exit", "bye"):
            print("Bot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()