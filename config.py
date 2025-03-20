from openai import OpenAI
import os
from dotenv import load_dotenv

# Configurações ElevenLabs
API_KEY_ELEVENLABS = "sk_048a9bc998e7e01a7b39625b967110e23d22645e100f9ceb"
VOICE_ID_ELEVENLABS = "21m00Tcm4TlvDq8ikWAM"

# Configurações gerais
PASTA_IMAGENS = "imagens_geradas"

def criar_cliente():
    return OpenAI(api_key="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")