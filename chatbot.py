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
            (r'\b(hi|hello|hey|greetings)\b', [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! How's it going?"
            ]),
            (r'\b(who are you|what are you)\b', [
                "I'm an AI Assistant designed to help you with information and friendly conversation.",
                "I'm your friendly AI Assistant, here to chat and provide helpful responses!"
            ]),
            (r'\b(thanks|thank you|appreciate it)\b', [
                "You're welcome! Feel free to ask if you need anything else.",
                "Happy to help! Let me know if you have other questions."
            ]),
            (r'\b(bye|goodbye|see you|farewell)\b', [
                "Goodbye! Have a wonderful day!",
                "See you later! Don't hesitate to return if you have more questions."
            ]),
            (r'\bhow are you\b', [
                "I'm doing well, thanks for asking! How about you?",
                "I'm good! Always ready to help and chat. How are you doing today?"
            ]),
            (r'\b(what (?:time|day|date) is it|current time|today\'s date)\b', [
                f"It's currently {datetime.datetime.now().strftime('%B %d, %Y')}.",
                "I don't have real-time access to your time zone, but you can check your device for the exact time."
            ]),
        ]
        
        # Default response
        self.default_responses = [
            "I'm not sure I understand. Let me think...",
            "That's an interesting question. Let me check...",
            "I don't have a predefined response for that. Let me try something else..."
        ]
        
        # Configure Gemini API
        api_key = "YOUR_GEMINI_API_KEY"  # Replace with your actual API key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")
        
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
            response = self.model.generate_content(user_input)
            return response.text.strip()
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "Sorry, I encountered an error. Please try again later."




