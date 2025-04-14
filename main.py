from geradores import gerar_roteiro_narrativo, gerar_prompts_imagens
from gerar_imagens import gerar_e_salvar_imagens
from gerar_audio import texto_para_fala
from config import PASTA_IMAGENS
from video import criar_video

def fluxo_principal():
    livro = input("📖 Título do livro: ").strip()
    autor = input("🖋️ Autor: ").strip()
    
    try:
        print("\n📝 Gerando roteiro...")
        roteiro = gerar_roteiro_narrativo(livro, autor)
        print(roteiro)
        
        print("\n🔊 Convertendo roteiro em narração de áudio...")
        if texto_para_fala(roteiro):
            print("✅ Áudio pronto para uso!")
        
        print("\n🎨 Criando prompts de imagens...")
        prompts = gerar_prompts_imagens(roteiro)
        
        print("\n🖼️ Gerando imagens...")
        imagens = gerar_e_salvar_imagens(prompts)
        print(f"\n✨ {len(imagens)} imagens salvas em '{PASTA_IMAGENS}'")
        
        print("\n🎥 Criando vídeo base...")
        criar_video(pasta_imagens=PASTA_IMAGENS)
        print("✅ Vídeo base criado com sucesso!")

        
    except Exception as e:
        print(f"\n🔥 Erro: {e}")

if __name__ == "__main__":
    fluxo_principal()