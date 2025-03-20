from moviepy.editor import *
import os
import re

def criar_video(pasta_imagens='imagens_geradas', audio_path='narracao.mp3', video_output='video.mp4', fps=24):
    try:
        # Carregar o áudio e obter duração
        audio = AudioFileClip(audio_path)
        duracao_total = audio.duration

        # Listar todas as imagens que seguem o padrão img_{n}.png
        padrao = re.compile(r'img_(\d+)\.png')
        imagens = sorted(
            [f for f in os.listdir(pasta_imagens) if padrao.match(f)],
            key=lambda x: int(padrao.match(x).group(1))
        )

        if not imagens:
            raise ValueError("Nenhuma imagem encontrada no formato img_{n}.png")

        # Calcular tempo por imagem
        tempo_por_imagem = duracao_total / len(imagens)

        # Criar lista de clips das imagens
        clips = []
        for img in imagens:
            img_path = os.path.join(pasta_imagens, img)
            clip = ImageClip(img_path).set_duration(tempo_por_imagem)
            clip = clip.crossfadein(0.5).crossfadeout(0.5)
            clips.append(clip)

        # Concatenar os clips
        video = concatenate_videoclips(clips, method="compose").set_audio(audio)

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
