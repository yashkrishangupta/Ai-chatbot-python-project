import os
from app import app

if __name__ == "__main__":
    # Use PORT environment variable if available (for cloud deployment)
    port = int(os.environ.get("PORT", 5000))
    
    # Set host to 0.0.0.0 to make the server publicly available
    # Turn off debug mode in production
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False if os.environ.get("ENVIRONMENT") == "production" else True
    )
