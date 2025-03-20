from openai import OpenAI
import os
from dotenv import load_dotenv

# Configurações ElevenLabs
API_KEY_ELEVENLABS = "api_key"
VOICE_ID_ELEVENLABS = "link"

# Configurações gerais
PASTA_IMAGENS = "imagens_geradas"

def criar_cliente():
    return OpenAI(api_key="api_key")