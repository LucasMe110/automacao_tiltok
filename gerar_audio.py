import requests
from config import API_KEY_ELEVENLABS, VOICE_ID_ELEVENLABS

def texto_para_fala(texto):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID_ELEVENLABS}"
    
    headers = {
        "xi-api-key": API_KEY_ELEVENLABS,
        "Content-Type": "application/json"
    }

    data = {
        "text": texto,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8
        }
    }

    resposta = requests.post(url, headers=headers, json=data)

    if resposta.status_code == 200:
        with open("narracao.mp3", "wb") as f:
            f.write(resposta.content)
        print("\n🔊 Narração de áudio gerada com sucesso! Salva como 'narracao.mp3'")
        return True
    else:
        print("\n🔇 Erro na geração de áudio:", resposta.text)
        return False