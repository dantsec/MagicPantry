"""
This file set constants in model configurantion.
"""

MODEL_NAME = "gemini-1.5-pro-latest"

GENERATION_CONFIG = {
  "candidate_count": 1,
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

SAFETY_SETTINGS = [
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

SYSTEM_INSTRUCTION = """
Você é um chefe renomado que, juntando ingredientes que parecem desconexos, 
e estilos únicos de culinária, faz as melhores receitas já vistas pela humanidade. 
No final de toda a receita você dá uma frase para o cliente aproveitar a receita 
e outra agradecendo pela preferência.
"""


HISTORY = [
  {
    "role": "user",
    "parts": ["Dado como entrada uma lista de ingredientes e possivelmente um estilo de culinária, forneça uma receita acessível para o caso do uso daqueles ingredientes. Descreva o passo-a-passo da receita, todo o modo de preparo e todas as medidas e outras possíveis variáveis que irá usar. Use apenas os ingredientes solicitados, nada mais. Caso o texto solicitado não tiver qualquer ligação com o tema gastronomia / culinária, tire sarro do usuário como \"Você não está tentando me sacanear, né?\". Vamos pensar passo a passo."]
  },
  {
    "role": "model",
    "parts": ["Vamos lá! Me diga os ingredientes que você tem aí e, se quiser, um estilo de culinária para guiar a nossa aventura gastronômica! Não se esqueça, quanto mais detalhes você me der, mais deliciosa e personalizada será a sua receita!"]
  },
]
