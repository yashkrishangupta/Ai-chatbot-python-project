document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const chatContainer = document.getElementById('chat-container');
    const typingIndicator = document.getElementById('typing-indicator');
    const suggestionButtons = document.querySelectorAll('.suggestion-btn');
    const statusIndicator = document.getElementById('status-indicator');
    
    // Auto-scroll to bottom of chat
    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    
    // Show the typing indicator
    function showTypingIndicator() {
        typingIndicator.classList.remove('d-none');
        scrollToBottom();
    }
    
    // Hide the typing indicator
    function hideTypingIndicator() {
        typingIndicator.classList.add('d-none');
    }
    
    // Update online status
    function updateStatus(isOnline) {
        if (isOnline) {
            statusIndicator.textContent = 'Online';
            statusIndicator.classList.remove('bg-danger');
            statusIndicator.classList.add('bg-success');
        } else {
            statusIndicator.textContent = 'Offline';
            statusIndicator.classList.remove('bg-success');
            statusIndicator.classList.add('bg-danger');
        }
    }
    
    // Add a message to the chat (user or bot)
    function addMessage(message, isUser) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add(isUser ? 'user-message' : 'bot-message', 'mb-3');
        
        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content');
        
        // Format links if present in the message
        const formattedMessage = formatLinks(message);
        
        const messagePara = document.createElement('p');
        messagePara.classList.add('mb-0');
        messagePara.innerHTML = formattedMessage;
        
        messageContent.appendChild(messagePara);
        messageDiv.appendChild(messageContent);
        
        // Add timestamp
        const timestamp = document.createElement('div');
        timestamp.classList.add('message-timestamp', 'small', 'text-muted', 'mt-1');
        
        const now = new Date();
        const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        
        timestamp.textContent = timeStr;
        
        if (isUser) {
            timestamp.style.textAlign = 'right';
            messageDiv.appendChild(timestamp);
        } else {
            timestamp.style.textAlign = 'left';
            messageDiv.appendChild(timestamp);
        }
        
        // Insert in chat container
        chatContainer.appendChild(messageDiv);
        scrollToBottom();
    }
    
    // Format links in text
    function formatLinks(text) {
        // Simple URL regex
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        return text.replace(urlRegex, function(url) {
            return '<a href="' + url + '" target="_blank" rel="noopener noreferrer">' + url + '</a>';
        });
    }
    
    // Send a message to the server and get a response
    async function sendMessage(message) {
        try {
            // Add user message to chat
            addMessage(message, true);
            
            // Clear input field
            messageInput.value = '';
            
            // Show typing indicator
            showTypingIndicator();
            
            // Random delay to simulate thinking (between 800ms and 2000ms)
            const thinkingTime = Math.floor(Math.random() * 1200) + 800;
            
            // Send the message to the server
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });
            
            // Parse the JSON response
            const data = await response.json();
            
            // Wait for the thinking time
            await new Promise(resolve => setTimeout(resolve, thinkingTime));
            
            // Hide typing indicator
            hideTypingIndicator();
            
            if (response.ok) {
                // Add bot response to chat
                addMessage(data.response, false);
            } else {
                // Handle error response
                addMessage(`Error: ${data.error || 'Failed to get response'}`, false);
                updateStatus(false);
            }
        } catch (error) {
            console.error('Error sending message:', error);
            hideTypingIndicator();
            addMessage('Sorry, there was an error processing your message. Please try again.', false);
            updateStatus(false);
            
            // Try to reconnect after 5 seconds
            setTimeout(() => {
                updateStatus(true);
            }, 5000);
        }
    }
    
    // Handle form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const message = messageInput.value.trim();
        if (message) {
            sendMessage(message);
        }
    });
    
    // Handle suggestion button clicks
    suggestionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const suggestionText = this.textContent.trim();
            messageInput.value = suggestionText;
            sendMessage(suggestionText);
        });
    });
    
    // Handle smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Focus input field on page load
    messageInput.focus();
    
    // Initial scroll to bottom
    scrollToBottom();
    
    // Check if we're at the chat section directly
    if (window.location.hash === '#chat-section') {
        setTimeout(() => {
            const chatSectionElement = document.querySelector('#chat-section');
            if (chatSectionElement) {
                chatSectionElement.scrollIntoView({
                    behavior: 'smooth'
                });
                messageInput.focus();
            }
        }, 500);
    }
});