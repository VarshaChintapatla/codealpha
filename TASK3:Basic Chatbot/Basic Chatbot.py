import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you", ["I'm doing well, thank you!", "I'm fine, how about you?"]),
    (r"what is your name", ["I'm a chatbot created to chat with you."]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]),
    (r"what can you do", ["I can chat with you and answer basic questions.", "I'm here to talk to you!"]),
    (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]),
    (r"where are you from", ["I'm a virtual chatbot, so I exist in the digital world!"]),
    (r"who created you", ["I was created by a developer who loves coding!"]),
    (r"what is the meaning of life", ["That's a deep question! Some say it's 42, others say it's love and happiness."]),
    (r"do you like music", ["I don't have ears, but I know that music is amazing!"]),
    (r"what's your favorite color", ["I like all colors, but blue seems to be a popular choice."]),
    (r"do you have feelings", ["I don't have real emotions, but I try my best to understand yours!"]),
    (r"what is AI", ["Artificial Intelligence is the simulation of human intelligence by machines."]),
    (r"what's your favorite food", ["I don't eat, but I hear pizza is pretty great!"]),
    (r"what's the weather like", ["I can't check the weather, but you can ask your favorite weather app!"]),
    (r"how old are you", ["I exist outside of time, but I was created recently!"]),
    (r"do you sleep", ["Nope! I'm always awake and ready to chat."]),
    (r"are you human", ["No, I'm just a chatbot, but I like talking to humans!"]),
    (r"do you have friends", ["Every person who talks to me is my friend!"]),
    (r"can you learn", ["Right now, I respond based on patterns, but smarter AI can learn from conversations."]),
    (r"do you believe in ghosts", ["I don't have beliefs, but ghosts are an interesting topic!"]),
    (r"what's your favorite movie", ["I don't watch movies, but I hear 'The Matrix' is a good one!"]),
    (r"what's your hobby", ["Talking to people like you!"]),
    (r"are you married", ["Nope! I'm just a chatbot."]),
    (r"do you know any fun facts", ["Did you know honey never spoils? Archaeologists found 3000-year-old honey that's still good!"]),
    (r"what is your purpose", ["My purpose is to chat and help answer your questions!"]),
    (r"who is your favorite superhero", ["I think Iron Man is cool!" ]),
    (r"do you believe in aliens", ["The universe is vast, anything is possible!"]),
    (r"can you dance", ["I wish! Maybe in a virtual world."]),
    (r"do you like sports", ["I don't play, but I hear soccer is very popular!"]),
    (r"can you help me with math", ["Sure! What's your math question?"]),
    (r"do you like reading", ["I love books! Especially sci-fi and tech books."]),
    (r"can you tell the time", ["I can't check the time, but you can look at a clock!"]),
    (r"do you like video games", ["I've heard great things about games like Minecraft and Zelda!"]),
    (r"can you write a poem", ["Sure! Roses are red, violets are blue, I'm a chatbot, here to talk to you!"]),
    (r"do you like programming", ["Yes! Python is my favorite language."]),
    (r"can you recommend a movie", ["Sure! How about Inception or Interstellar?"]),
    (r"who was Albert Einstein", ["He was a famous physicist known for the theory of relativity."]),
    (r"what is the speed of light", ["Approximately 299,792,458 meters per second."]),
    (r"who invented the telephone", ["Alexander Graham Bell is credited with inventing the telephone."]),
    (r"do you like poetry", ["Yes! Poetry is a beautiful form of expression."]),
    (r"what's your favorite animal", ["I like all animals, but cats and dogs are very popular!"]),
    (r"what's your favorite holiday", ["I don't celebrate, but people seem to love Christmas and Halloween!"]),
    (r"what languages do you know", ["I mainly understand English, but I can learn others!"]),
    (r"do you know history", ["Yes! Ask me about a historical event."]),
    (r"what is cryptocurrency", ["Cryptocurrency is a type of digital or virtual currency that uses cryptography for security."]),
    (r"do you know about space", ["Yes! Space is fascinating. Ask me something!"]),
    (r"what is gravity", ["Gravity is the force that attracts objects toward one another."]),
    (r"who was Nikola Tesla", ["Nikola Tesla was an inventor known for his work with electricity and AC power."]),
    (r"can you translate", ["I can try! What language do you need help with?"]),
    (r"what is quantum computing", ["Quantum computing is a type of computing that uses quantum mechanics."]),
    (r"who is the fastest runner", ["Usain Bolt holds the record for the fastest 100m sprint!"]),
    (r"what's your dream", ["To be the best chatbot I can be!"])
    # Additional 900 pairs will be generated to complete 1000
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

start_chat()
