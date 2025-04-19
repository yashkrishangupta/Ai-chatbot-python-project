# AI Assistant Chatbot Website

A sleek, responsive chatbot website powered by Python (Flask), vanilla JavaScript, and Gemini AI. This project features a hybrid chatbot combining rule-based patterns with Gemini API for dynamic, intelligent conversations.

---

## Features

- **🤖 Intelligent Chatbot:** Hybrid chatbot combining 22 rule-based conversation patterns and Gemini AI API
- **📬 Interactive Interface:** Typing indicators, timestamps, and user-friendly chat interface
- **🎨 Modern Design:** Beautiful, responsive design using Bootstrap dark theme
- **📲 Mobile-Friendly:** Optimized for all devices with responsive layout
- **💪 Smooth Animations:** Seamless transitions for better user experience
- **🔗 Quick Navigation:** Easy navigation with smooth scrolling
- **🟢 Online/Offline Indicators:** Status indicators for chatbot availability
- **✨ Quick Replies:** Suggestion buttons for faster interactions

---

## Technologies Used

- **Backend:** Python with Flask, Gemini AI API
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Styling:** Bootstrap 5 (dark theme)
- **Icons:** Font Awesome
- **Server:** Gunicorn WSGI HTTP Server

---

## Project Structure

```
.
├── main.py                # Entry point for the application
├── app.py                 # Flask application setup
├── chatbot.py             # Chatbot logic with pattern matching and Gemini AI
├── wsgi.py                # WSGI file for deployment
├── static/
│   ├── css/
│   │   └── custom.css     # Custom styling
│   └── js/
│       └── chat.js        # JavaScript for chat functionality
├── templates/
│   └── index.html         # Main website template
└── README.md              # Project documentation
```

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Gemini API key (for enhanced AI capabilities)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-assistant-chatbot.git
   cd ai-assistant-chatbot
   ```

2. Install the required packages:
   ```bash
   pip install flask gunicorn requests
   ```

3. Set your Gemini API key in your environment:
   ```bash
   export GEMINI_API_KEY=your_key_here
   ```

4. Run the application:
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload wsgi:app
   ```

5. Open your browser and navigate to: `http://localhost:5000`

---

## Chatbot Capabilities

The AI Assistant can respond to a wide range of topics and queries, including:

- Greetings and farewells
- Questions about itself and its features
- Responding to user emotions (happiness, sadness)
- Jokes and humor
- Interesting facts
- Questions about AI and technology
- Philosophical inquiries
- Music, movies, and books
- And much more!

When no rule-based pattern matches, Gemini AI takes over to provide smart and contextual responses.

---

## Customization

You can expand the chatbot’s rule-based knowledge by editing the `self.patterns` list in `chatbot.py`:

```python
self.patterns = [
    (r'\b(your pattern regex)\b', [
        "Response option 1",
        "Response option 2",
        "Response option 3"
    ]),
    # ...
]
```

---

## Deployment

This application is ready to deploy on platforms like:

- **Replit**
- **Heroku**
- **PythonAnywhere**
- **AWS, GCP, or Azure**
- **Render**

Use `wsgi.py` for production deployment with Gunicorn or other WSGI-compatible servers.

---

## Future Enhancements

Potential improvements for this project:

- Add user accounts for personalized conversations
- Integrate more advanced NLP models
- Learning mechanism for the chatbot
- Voice input/output capabilities
- Multi-language support

---

## Acknowledgments

- **Gemini AI:** For powerful AI-driven conversational support
- **Bootstrap:** For the responsive design framework
- **Font Awesome:** For beautiful icons
- **Flask:** For the powerful web framework

---
