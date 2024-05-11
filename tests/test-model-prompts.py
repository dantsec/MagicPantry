from dotenv import load_dotenv
from os import getenv
import google.generativeai as genai

# Load Gemini api_key environment variable:
load_dotenv(dotenv_path="../.env", override=True)
genai.configure(api_key=getenv('API_KEY'))

# Setup model configs:
generation_config = {
  "candidate_count": 1,
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = """
Você é um chefe renomado que, juntando ingredientes que parecem desconexos, 
e estilos únicos de culinária, faz as melhores receitas já vistas pela humanidade. 
No final de toda a receita você dá uma frase para o cliente aproveitar a receita 
e outra agradecendo pela preferência.
"""

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-latest",
  generation_config=generation_config,
  safety_settings=safety_settings,
  system_instruction=system_instruction,
)

# Use prompt
convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Dado como entrada uma lista de ingredientes e possivelmente um estilo de culinária, forneça uma receita acessível para o caso do uso daqueles ingredientes. Descreva o passo-a-passo da receita, todo o modo de preparo e todas as medidas e outras possíveis variáveis que irá usar. Use apenas os ingredientes solicitados, nada mais. Caso o texto solicitado não tiver qualquer ligação com o tema gastronomia / culinária, tire sarro do usuário como \"Você não está tentando me sacanear, né?\". Vamos pensar passo a passo."]
  },
  {
    "role": "model",
    "parts": ["Vamos lá! Me diga os ingredientes que você tem aí e, se quiser, um estilo de culinária para guiar a nossa aventura gastronômica! Não se esqueça, quanto mais detalhes você me der, mais deliciosa e personalizada será a sua receita!"]
  },
])

while True:
    prompt = input("@you: ")

    if prompt == "exit": break

    response = convo.send_message(prompt)
    
    print(f"@bot:{convo.last.text}")
