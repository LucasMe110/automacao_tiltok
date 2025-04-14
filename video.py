from moviepy.editor import *
import os

def criar_video(pasta_imagens='imagens_geradas', audio_path='narracao.mp3', video_output='video.mp4', fps=24):
    try:
        # Carregar o áudio e obter duração
        audio = AudioFileClip(audio_path)
        duracao_total = audio.duration
        
        # Listar e ordenar as imagens geradas
        imagens = sorted([
            os.path.join(pasta_imagens, img) 
            for img in os.listdir(pasta_imagens) 
            if img.endswith('.png')
        ], key=lambda x: int(x.split('_')[-1].split('.')[0]))
        
        if not imagens:
            raise Exception("Nenhuma imagem encontrada para criar o vídeo")
            
        tempo_por_imagem = duracao_total / len(imagens)

        # Criar lista de clips das imagens
        clips = []
        for img_path in imagens:
            clip = ImageClip(img_path).set_duration(tempo_por_imagem)
            clip = clip.crossfadein(0.5).crossfadeout(0.5)
            clips.append(clip)

        # Concatenar os clips
        video = concatenate_videoclips(clips, method="compose")
        video = video.set_audio(audio)

        # Escrever arquivo final
        video.write_videofile(
            video_output,
            fps=fps,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True
        )

        print(f"Vídeo criado com sucesso: {video_output}")
        return True
    except Exception as e:
        print(f"Erro na criação do vídeo: {str(e)}")
        return False

if __name__ == "__main__":
    criar_video()