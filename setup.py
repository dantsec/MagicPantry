from os import system as shell

print("Setup started...")
print("Downloading packages...")

"""
Get required packages and download them.
"""

with open("./requirements.txt", "r") as requirements:
    required_packages = [line.strip() for line in requirements.readlines()]

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
