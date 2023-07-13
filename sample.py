def greet():
    print("Hello! How can I assist you today?")

def get_user_input():
    return input("> ")

def process_input(user_input):
    if user_input.lower() == "hello":
        print("Hello there!")
    elif user_input.lower() == "goodbye":
        print("Goodbye! Have a great day!")
        return False  # Return False to end the conversation
    else:
        print("I'm sorry, I didn't understand that.")

    return True  # Return True to continue the conversation

if __name__ == "__main__":
    greet()
    conversation_active = True

    while conversation_active:
        user_input = get_user_input()
        conversation_active = process_input(user_input)
