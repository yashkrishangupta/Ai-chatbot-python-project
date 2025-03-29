import os
import logging
from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key-for-development")

# Initialize chatbot
chatbot = ChatBot()

@app.route('/')
def index():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Process chat messages and return bot response."""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        # Get response from chatbot
        bot_response = chatbot.get_response(user_message)
        
        return jsonify({
            "response": bot_response
        })
    except Exception as e:
        logging.error(f"Error processing message: {str(e)}")
        return jsonify({"error": "Failed to process your message"}), 500