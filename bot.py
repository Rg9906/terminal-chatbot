print("Chatbot started. Type 'exit' to quit.")

last_message = ""

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Alright. See you.")
        break

    if user_input == last_message:
        print("Bot: You already said that.")
    elif "hello" in user_input.lower():
        print("Bot: Hi. You seem awake.")
    elif "tired" in user_input.lower():
        print("Bot: Same. What happened?")
    else:
        print("Bot: Interesting.")

    last_message = user_input
