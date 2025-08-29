def chatbot():
    print("🤖 Chatbot: Hi! I'm your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Chatbot: Hello! How are you?")
        elif user_input in ["i'm fine", "fine", "good"]:
            print("Chatbot: I'm glad to hear that!")
        elif user_input == "how are you":
            print("Chatbot: I'm just a bot, but I'm doing great! 😄")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day 👋")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
