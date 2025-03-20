from openai import OpenAI
import os
from dotenv import load_dotenv

# Configurações ElevenLabs
API_KEY_ELEVENLABS = ""
VOICE_ID_ELEVENLABS = ""

# Configurações gerais
PASTA_IMAGENS = "imagens_geradas"

def criar_cliente():
    return OpenAI(api_key="")