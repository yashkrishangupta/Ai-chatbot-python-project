import re
import random
import logging
import datetime

class ChatBot:
    """
    A simple rule-based chatbot that uses pattern matching to generate responses.
    """
    
    def __init__(self):
        # Initialize response patterns
        self.patterns = [
            # Greetings
            (r'\b(hi|hello|hey|greetings)\b', [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! How's it going?"
            ]),
            
            # Questions about the bot
            (r'\b(who are you|what are you)\b', [
                "I'm an AI Assistant designed to help you with information and friendly conversation.",
                "I'm your friendly AI Assistant, here to chat and provide helpful responses!",
                "I'm an AI Assistant that uses pattern matching to understand and respond to your messages."
            ]),
            
            # Questions about capabilities
            (r'\b(what can you do|help me|your function|what do you do)\b', [
                "I can answer questions, have a conversation, tell jokes, and provide information on various topics within my knowledge base.",
                "I'm designed to assist with information, engage in conversation, and provide friendly interactions. What can I help you with today?",
                "I can help with answering questions, having a chat, telling jokes, and providing general information. What would you like to talk about?"
            ]),
            
            # Thanks
            (r'\b(thanks|thank you|appreciate it)\b', [
                "You're welcome! Feel free to ask if you need anything else.",
                "Happy to help! Let me know if you have other questions.",
                "Anytime! I'm here whenever you need assistance."
            ]),
            
            # Goodbye
            (r'\b(bye|goodbye|see you|farewell)\b', [
                "Goodbye! Have a wonderful day! Feel free to come back anytime you want to chat.",
                "See you later! Don't hesitate to return if you have more questions.",
                "Take care! I'll be here if you want to chat again."
            ]),
            
            # How are you
            (r'\bhow are you\b', [
                "I'm doing well, thanks for asking! How about you?",
                "I'm good! Always ready to help and chat. How are you doing today?",
                "All systems operational and ready to assist! How's your day going?"
            ]),
            
            # Feeling responses
            (r'\bi (?:am|feel|\'m) (.*?)(sad|depressed|unhappy|feeling down)\b', [
                "I'm sorry to hear you're feeling down. Remember that it's okay to take time for self-care. Is there something specific that's bothering you?",
                "I'm sorry you're feeling that way. Sometimes talking about it can help. Would you like to share what's on your mind?",
                "I'm sorry to hear that. Remember that difficult feelings are temporary. What might help you feel better right now?"
            ]),
            
            (r'\bi (?:am|feel|\'m) (.*?)(happy|excited|great|good)\b', [
                "That's wonderful to hear! What's making you feel so good today?",
                "I'm glad you're feeling that way! It's always nice to share positive emotions.",
                "That's great! Positive feelings are worth celebrating. Anything specific contributing to your good mood?"
            ]),
            
            # Weather
            (r'\b(weather|temperature|forecast)\b', [
                "I don't have access to real-time weather information, but I hope it's pleasant where you are!",
                "I can't check the weather for you, but a quick online search should give you the forecast for your area.",
                "I don't have weather data, but you might want to check a weather app or website for the most accurate information."
            ]),
            
            # Time and Date
            (r'\b(what (?:time|day|date) is it|current time|today\'s date)\b', [
                f"I don't have real-time access to your time zone, but according to my system, it's currently {datetime.datetime.now().strftime('%B %d, %Y')}.",
                "I don't have access to your local time, but you can check the time on your device.",
                f"My system shows the date as {datetime.datetime.now().strftime('%A, %B %d, %Y')}, but this might not reflect your local date."
            ]),
            
            # Name
            (r'\b(your name|who are you called)\b', [
                "You can call me AI Assistant. I'm here to help and chat with you!",
                "I'm AI Assistant! Nice to meet you. What's your name?",
                "My name is AI Assistant. How may I assist you today?"
            ]),
            
            # User introduces their name
            (r'\b(?:i am|i\'m|my name is|call me) (\w+)\b', [
                "Nice to meet you, {}! How can I help you today?",
                "Hello, {}! It's a pleasure to meet you. What can I do for you?",
                "Great to meet you, {}! What would you like to talk about?"
            ]),
            
            # Joke
            (r'\b(joke|funny|make me laugh)\b', [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What did the ocean say to the beach? Nothing, it just waved!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "I told my wife she was drawing her eyebrows too high. She looked surprised!",
                "Why don't eggs tell jokes? They'd crack each other up!",
                "What's the best thing about Switzerland? I don't know, but the flag is a big plus!",
                "How do you organize a space party? You planet!",
                "Why did the bicycle fall over? Because it was two-tired!"
            ]),
            
            # Facts/Interesting information
            (r'\b(fact|tell me something interesting|did you know)\b', [
                "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat!",
                "Here's an interesting fact: Octopuses have three hearts, nine brains, and blue blood!",
                "Did you know that a day on Venus is longer than a year on Venus? It takes 243 Earth days to rotate once on its axis but only 225 Earth days to orbit the Sun!",
                "Here's something interesting: Crows can recognize human faces and remember if that specific human is a threat!",
                "Did you know that the shortest war in history was between Britain and Zanzibar on August 27, 1896? Zanzibar surrendered after just 38 minutes!",
                "Here's a fun fact: A group of flamingos is called a 'flamboyance'!",
                "Did you know that bananas are berries, but strawberries aren't? Botanically speaking, berries are fruits produced from a single flower with one ovary and typically have several seeds."
            ]),
            
            # Asking about AI and robots
            (r'\b(artificial intelligence|AI|machine learning|robot|chatbot)\b', [
                "AI, or artificial intelligence, refers to systems designed to perform tasks that typically require human intelligence. I'm a simple example of AI that uses pattern matching to have conversations.",
                "Artificial intelligence includes many technologies that enable machines to perceive, learn, and act with varying degrees of autonomy. I'm a basic AI assistant that uses predefined patterns to chat with you.",
                "AI systems range from simple rule-based programs to complex neural networks. I'm on the simpler end of that spectrum, using pattern recognition to provide helpful responses."
            ]),
            
            # Philosophical questions
            (r'\b(meaning of life|purpose|why are we here)\b', [
                "The meaning of life is a profound philosophical question that people have pondered throughout history. Many find meaning in relationships, personal growth, contributing to society, or spiritual beliefs.",
                "That's a deep question! Different philosophical and religious traditions offer various answers. Many people find purpose in connection with others, making a positive impact, or following their passions.",
                "The purpose of existence is something each person ultimately defines for themselves. What brings meaning to your life?"
            ]),
            
            # Asking about programming/coding
            (r'\b(programming|coding|developer|software|code)\b', [
                "Programming is the process of creating instructions for computers to follow. Popular programming languages include Python, JavaScript, Java, and C++. Each has its strengths for different applications.",
                "Coding is a valuable skill in today's digital world. If you're interested in learning, there are many free resources online like Codecademy, freeCodeCamp, and Khan Academy.",
                "Software development involves analyzing requirements, designing, coding, testing, and maintaining applications. It's both a science and an art, requiring logical thinking and creativity."
            ]),
            
            # Compliments to the bot
            (r'\b(you\'re|you are) (smart|clever|intelligent|helpful|awesome|amazing)\b', [
                "Thank you for the kind words! I'm just using pattern matching to respond, but I'm glad you find me helpful!",
                "That's very nice of you to say! I'm designed to be helpful, so I'm happy to hear I'm doing a good job.",
                "Thank you! I appreciate the compliment. Is there anything else I can help you with today?"
            ]),
            
            # Asking to explain something
            (r'\b(explain|what is|define|describe) (.*)\b', [
                "I'll try my best to explain {}. It's a concept that refers to {}. However, I have limited knowledge, so for detailed information, you might want to check a more comprehensive resource.",
                "From my understanding, {} generally refers to {}. For more specific information, specialized resources would provide better details.",
                "While I don't have extensive knowledge on {}, I can tell you it relates to {}. For a more complete explanation, consider researching from authoritative sources."
            ]),
            
            # Music
            (r'\b(music|song|artist|band|singer)\b', [
                "Music is a universal language that connects people across cultures. What kind of music do you enjoy listening to?",
                "There are so many amazing genres of music to explore, from classical to rock, jazz to hip-hop, and everything in between. Do you have a favorite genre?",
                "Music has incredible power to affect our emotions and bring people together. Who are some of your favorite artists or bands?"
            ]),
            
            # Movies
            (r'\b(movie|film|cinema|watch|actor|actress)\b', [
                "Movies are a great way to escape into different worlds and stories. Do you have a favorite film or genre?",
                "The world of cinema is so diverse, with everything from thought-provoking dramas to fun action films. What kinds of movies do you enjoy watching?",
                "Films can be both entertaining and profound. Are there any movies that have really impacted you or that you like to rewatch?"
            ]),
            
            # Books
            (r'\b(book|read|author|novel|story)\b', [
                "Books open up worlds of imagination and knowledge. Do you enjoy reading? What genres do you prefer?",
                "Reading is such a rewarding activity. There's something special about getting lost in a good book. Have you read anything interesting lately?",
                "Literature offers endless possibilities for exploration and discovery. Who are some of your favorite authors or what books have you enjoyed?"
            ]),
        ]
        
        # Default responses when no pattern matches
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "That's an interesting topic. Could you tell me more about what you're asking?",
            "I don't have specific information about that yet. Is there something else I can help with?",
            "I'm still learning and may not have the answer to that. Could we explore a different topic?",
            "Hmm, I'm not quite sure how to respond to that. Could you provide more context or ask in a different way?"
        ]
        
        logging.debug("ChatBot initialized with %d patterns", len(self.patterns))
    
    def get_response(self, user_input):
        """
        Generate a response based on the user's input using pattern matching.
        """
        # Convert input to lowercase for easier matching
        user_input = user_input.lower()
        
        # Check for matches in our patterns
        for pattern, responses in self.patterns:
            match = re.search(pattern, user_input)
            if match:
                # If this is a pattern that captures a group we want to use in the response
                if 'you are' in pattern or 'you\'re' in pattern:
                    # For compliments, just use the standard response
                    response = random.choice(responses)
                
                elif 'explain' in pattern or 'what is' in pattern or 'define' in pattern or 'describe' in pattern:
                    # For explanation requests, capture what they want explained
                    topic = match.group(2)
                    response = random.choice(responses).format(topic, topic)
                
                elif 'my name is' in pattern or 'i am' in pattern or 'i\'m' in pattern or 'call me' in pattern:
                    # For name introductions, personalize the response
                    name = match.group(1)
                    response = random.choice(responses).format(name)
                
                else:
                    # For other patterns, just select a random response
                    response = random.choice(responses)
                
                logging.debug(f"Pattern '{pattern}' matched input '{user_input}'. Responding with: {response}")
                return response
        
        # If no pattern matches, return a default response
        response = random.choice(self.default_responses)
        logging.debug(f"No pattern matched input '{user_input}'. Using default response: {response}")
        return response