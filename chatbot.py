import re
import random
import logging
import datetime
import google.generativeai as genai

class ChatBot:
    """
    A chatbot that first tries rule-based responses and falls back to Google's Gemini AI if no pattern matches.
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
            
            # Questions about the bot owner
            (r'\b(who (is|’s) your (owner|host))\b', 
             ["Yash Krishan Gupta"]),

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
        ]
        
        # Default response
        self.default_responses = [
            "I'm not sure I understand. Let me think...",
            "That's an interesting question. Let me check...",
            "I don't have a predefined response for that. Let me try something else..."
        ]
        
        # Configure Gemini API
        api_key = "AIzaSyA9Q4j0JqXyR50Xj-uYgfM49nbQoMg7pMs"
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")
        self.gemini_prompt = "You are a helpful and concise AI chatbot. Keep responses short ,relevant and give real time data too if asked."
        logging.debug("ChatBot initialized with rule-based responses and Gemini AI fallback.")
    
    def get_response(self, user_input):
        """
        Generate a response using pattern matching first, then fallback to Gemini AI if no match is found.
        """
        user_input = user_input.lower()
        
        # Check for pattern matches
        for pattern, responses in self.patterns:
            if re.search(pattern, user_input):
                response = random.choice(responses)
                logging.debug(f"Pattern matched: '{pattern}'. Responding with: {response}")
                return response
        
        # If no pattern matched, use Gemini API
        try:
            logging.debug("No pattern matched. Using Gemini AI for response.")
            response = self.model.generate_content(f"{self.gemini_prompt}\nUser: {user_input}\nAI:")
            return response.text.strip()
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "Sorry, I encountered an error. Please try again later."




