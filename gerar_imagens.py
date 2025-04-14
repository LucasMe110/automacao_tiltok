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
    cliente = criar_cliente()
    prompts = processar_prompts(prompts_texto)[:num_imagens]
    os.makedirs(PASTA_IMAGENS, exist_ok=True)
    
    caminhos_imagens = []
    success_count = 0  # Contador de imagens geradas com sucesso
    
    for idx, prompt in enumerate(prompts, 1):
        try:
            # Geração via DALL-E 3
            resposta = cliente.images.generate(
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
            
            success_count += 1
            nome_arquivo = f"img_{success_count}.png"  # Usa o contador de sucessos
            caminho_completo = os.path.join(PASTA_IMAGENS, nome_arquivo)
            
            with Image.open(BytesIO(resposta_img.content)) as img:
                img.save(caminho_completo)
            
            caminhos_imagens.append(caminho_completo)
            print(f"✅ Imagem {success_count} gerada: {nome_arquivo}")
            
        except Exception as e:
            # Mostra mais detalhes do erro da API
            error_msg = str(e)
            if hasattr(e, 'response') and e.response:
                error_msg += f" - {e.response.text}"
            print(f"❌ Erro no prompt {idx}: {error_msg[:150]}...")
            continue  # Continua para o próximo prompt

    return caminhos_imagens



# Processamento dos prompts (split por linhas)
def processar_prompts(texto):
    linhas = texto.strip().split('\n')
    return [linha.strip() for linha in linhas if linha.strip()]

# Configurações
PASTA_IMAGENS = "imagens_geradas"  # Pasta para salvar as imagens

# Lista de prompts (um por linha)
prompts_texto = """
Um cavalo alado sobrevoando montanhas nevadas
Uma cidade cyberpunk em um planeta alienígena
Retrato de um samurai digital com neon
Um jardim flutuante com plantas bioluminescentes
"""

