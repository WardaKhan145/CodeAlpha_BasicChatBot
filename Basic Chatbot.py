def get_bot_response(user_input):
    """
    Returns a predefined reply based on the user's input.
    Using .lower() ensures the chatbot understands 'Hello', 'HELLO', or 'hello'.
    """
    user_input = user_input.strip().lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I didn't quite catch that. Could you try saying 'hello', 'how are you', or 'bye'?"


def main():
    print("\n")
    print("                              Welcome to the Rule-Based Chatbot!   ")
    print("                                (Type 'bye' to exit the chat)      ")
    print("\n")
    

    while True:
        user_message = input("You: ")
        
        bot_message = get_bot_response(user_message)
        
        print(f"Bot: {bot_message}\n")
        
        if "bye" in user_message.lower() or "goodbye" in user_message.lower():
            break

if __name__ == "__main__":
    main()
