def sanitize(txt):
    return txt.strip().lower()
responses = {
"what is ai": "AI stands for Artificial Intelligence.",
"what is python": "Python is a popular programming language.",
"what is machine learning": "Machine Learning is a branch of AI.",
"what can you do": "I can answer simple predefined questions.",
"thank you": "You are welcome!",
"good morning": "Good Morning!",
"good night": "Good Night!"
}
def getresponse(user):
    if user == "hi":
        return "Hello! Nice to meet you."
    elif user == "hello":
        return "Hi there! Welcome to the chatbot."
    elif user == "hey":
        return "Hey! How can I help you?"
    elif user == "how are you":
        return "I am fine. Thank you for asking."
    elif user == "what is your name":
        return "I am a Rule-Based AI Chatbot."
    elif user == "who created you":
        return "I was created by Yaswanth using Python."
    elif user == "where are you from":
        return "I live inside this Python program."
    elif user == "are you a human":
        return "No, I am a chatbot."
    elif user == "help":
        return """'''Available Commands:\nhi\nhello\nhey\nhow are you\nwhat is your name\nwho created you\nwhere are you from\nare you a human\nwhat is ai\nwhat is python\nwhat is machine learning\nthank you\nbye'''"""
    elif user in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day."
    else:
        return responses.get(user,"Sorry, I don't understand that command.")
print("      CHATBOT       ")
print("===================================")
print("Type 'help' to view commands.")
print("Type 'bye' to exit.")
while True:
    usrinput = input("You: ")
    aninput = sanitize(usrinput)
    response = getresponse(aninput)
    print("Bot:", response)
    if aninput in ["bye", "exit", "quit"]:
        break
print("chatbot was ended successfully!")
