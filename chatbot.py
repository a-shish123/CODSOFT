import re

# Define patterns and corresponding responses
patterns_and_responses = [
    (r"(?:hi|hello|hey)\b", "Hello! How can I help you?"),
    (r"\b(bye|goodbye)\b", "Goodbye! Have a great day!"),
    (r"\b(?:how are you|how's it going)\b", "I'm just a bot, but I'm here to assist you!"),
    (r"\bwhat's your name\b", "I'm a chatbot, you can call me ChatBot."),
    (r"\b(?:thank you|thanks)\b", "You're welcome! Feel free to ask if you have more questions."),
    (r"\b(?:help|support)\b", "Sure, I'm here to help! What do you need assistance with?"),
    (r"\b(?:weather)\b", "I'm not equipped to provide real-time information, but you can check a weather website or app."),
    (r"\b(?:age)\b", "I don't have an age. I'm a program created to assist with information."),
    (r".*", "I'm sorry, I don't have an appropriate response for that.")
]

# Compile regular expressions
compiled_patterns_and_responses = [(re.compile(pattern, re.IGNORECASE), response) for pattern, response in patterns_and_responses]

# Chatbot function
def simple_chatbot(user_input):
    for pattern, response in compiled_patterns_and_responses:
        if re.match(pattern, user_input):
            return response

# Main loop
print("ChatBot: Hi there! I'm here to help. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye! Have a great day!")
        break
    response = simple_chatbot(user_input)
    print("ChatBot:", response)
