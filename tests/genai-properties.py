import google.generativeai as genai
from dotenv import load_dotenv
from os import getenv

load_dotenv()

genai.configure(api_key=getenv('GOOGLE_GEMINI_API_KEY'))

for item in genai.list_models():
    if 'generateContent' in item.supported_generation_methods:
        print(item.name[7:])

"""
gemini-1.0-pro
gemini-1.0-pro-001
gemini-1.0-pro-latest
gemini-1.0-pro-vision-latest
gemini-1.5-pro-latest
gemini-pro
gemini-pro-vision
"""