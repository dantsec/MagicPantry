from os import system as shell

print("Setup started...")
print("Downloading packages...")

"""
Set required packages and download them.
"""
required_packages = [
    "streamlit==1.34.0",
    "python-dotenv==1.0.1",
    "google-generativeai==0.5.2",
]

for package in required_packages:
    shell(f'pip install -q -U {package} --break-system-package')

print("Packages downloaded...")

"""
Create .env file
"""
api_key = input("Paste your Gemini API_KEY: ")

with open('./.env', 'w+') as env_file:
    env_file.write(f"GOOGLE_GEMINI_API_KEY='{api_key}'\n")

print("Setup finished...")
