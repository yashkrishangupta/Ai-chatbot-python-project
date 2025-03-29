# AI Assistant Chatbot Website

A sleek, responsive chatbot website powered by Python (Flask) and vanilla JavaScript. This project features a rule-based AI assistant that engages in dynamic conversations, answers questions, tells jokes, and provides information on a variety of topics.

---

## Features

- **🤖 Intelligent Chatbot:** Rule-based chatbot with 22 conversation patterns
- **📬 Interactive Interface:** Typing indicators, timestamps, and user-friendly chat interface
- **🎨 Modern Design:** Beautiful, responsive design using Bootstrap dark theme
- **📲 Mobile-Friendly:** Optimized for all devices with responsive layout
- **💪 Smooth Animations:** Seamless transitions for better user experience
- **🔗 Quick Navigation:** Easy navigation with smooth scrolling
- **🟢 Online/Offline Indicators:** Status indicators for chatbot availability
- **✨ Quick Replies:** Suggestion buttons for faster interactions

---

## Technologies Used

- **Backend:** Python with Flask
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
├── chatbot.py             # Chatbot logic with pattern matching
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

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-assistant-chatbot.git
   cd ai-assistant-chatbot
   ```

2. Install the required packages:
   ```bash
   pip install flask gunicorn
   ```

3. Run the application:
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   ```

4. Open your browser and navigate to: `http://localhost:5000`

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
- Topics like music, movies, and books
- And much more!

---

## Customization

Expand the chatbot's knowledge by adding new patterns to the `self.patterns` list in `chatbot.py`:

```python
self.patterns = [
    # Add your new pattern here
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

---

## Future Enhancements

Potential improvements for this project:

- Add user accounts for personalized conversations
- Integrate advanced NLP models for smarter interactions
- Add real-time data access for weather, news, and more
- Implement a learning mechanism for the chatbot
- Add voice input/output capabilities
- Enable multi-language support

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments

- **Bootstrap:** For the responsive design framework
- **Font Awesome:** For beautiful icons
- **Flask:** For the powerful web framework

---

Enjoy your new AI Assistant! If you have any questions or feedback, feel free to open an issue or submit a pull request.

