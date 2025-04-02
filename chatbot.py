import google.generativeai as genai
import logging

class ChatBot:
    """
    A chatbot that uses Google's Gemini API to generate responses dynamically.
    """

    def __init__(self, api_key):
        # Configure Gemini API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")  # Use an appropriate Gemini model
        logging.debug("ChatBot initialized with Gemini API.")

    def get_response(self, user_input):
        """
        Generate a response using the Gemini AI model.
        """
        try:
            response = self.model.generate_content(user_input)
            return response.text.strip()
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "Sorry, I encountered an error. Please try again later."

api_key = "AIzaSyA9Q4j0JqXyR50Xj-uYgfM49nbQoMg7pMs"  
chatbot = ChatBot(api_key)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("ChatBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("ChatBot:", response)
