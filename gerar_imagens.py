import re
import requests
from io import BytesIO
from PIL import Image
from config import criar_cliente, PASTA_IMAGENS
import os 
def processar_prompts(texto_prompts):
    """Extrai prompts PT-BR do texto gerado"""
    padrao = r"\[PT-BR\]:\s*([\s\S]+?)(?=\n\d+\.|\Z)"
    return re.findall(padrao, texto_prompts, re.DOTALL)

def gerar_e_salvar_imagens(prompts_texto, num_imagens=10):
    """Gera e salva imagens baseadas nos prompts"""
    cliente = criar_cliente()  # CORREÇÃO: chama a função para criar o cliente
    prompts = processar_prompts(prompts_texto)[:num_imagens]
    os.makedirs(PASTA_IMAGENS, exist_ok=True)
    
    caminhos_imagens = []
    for idx, prompt in enumerate(prompts, 1):
        try:
            # Geração via DALL-E 3
            resposta = cliente.images.generate(  # AGORA FUNCIONA
                model="dall-e-3",
                prompt=f"{prompt} Estilo hyper-realista, Octane Render, 8K",
                size="1024x1792",
                quality="hd",
                n=1
            )
            
            # Download e salvamento
            url = resposta.data[0].url
            resposta_img = requests.get(url)
            resposta_img.raise_for_status()
            
            nome_arquivo = f"img_{idx}.png"
            caminho_completo = os.path.join(PASTA_IMAGENS, nome_arquivo)
            
            with Image.open(BytesIO(resposta_img.content)) as img:
                img.save(caminho_completo)
            
            caminhos_imagens.append(caminho_completo)
            print(f"✅ Imagem {idx} gerada: {nome_arquivo}")
            
        except Exception as e:
            print(f"❌ Erro no prompt {idx}: {str(e)[:100]}...")

    return caminhos_imagens
