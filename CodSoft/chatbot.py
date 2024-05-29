import re

def get_response(user_input):
    
    user_input = user_input.lower()
    
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! How can I help you today?"
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm a chatbot, so I don't have feelings, but I'm here to help you!"
    elif re.search(r'\bwhat is your name\b', user_input):
        return "I'm a simple rule-based chatbot created by a programmer."
    elif re.search(r'\bbye\b|\bexit\b', user_input):
        return "Goodbye! Have a great day!"
    elif re.search(r'\bhelp\b', user_input):
        return "Sure, I'm here to help. What do you need assistance with?"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def run_chatbot():
    print("Welcome to the rule-based chatbot. Type 'bye' or 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot: " + response)
        if response == "Goodbye! Have a great day!":
            break

if __name__ == "__main__":
    run_chatbot()
