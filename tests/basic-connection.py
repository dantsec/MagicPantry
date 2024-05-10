from dotenv import load_dotenv
import google.generativeai as genai
from os import getenv

load_dotenv(override=True)

# API Connection
genai.configure(api_key=getenv('GOOGLE_GEMINI_API_KEY'))

# AI Config
model = genai.GenerativeModel('gemini-1.0-pro-latest')

# Start Chatbot
convo = model.start_chat(history=[])

# Execute a prompt
response = convo.send_message('1 + 1 = ?')

# Get the AI output
print(response.text)

"""
2
"""
