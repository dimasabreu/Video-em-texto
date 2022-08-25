from moviepy.editor import *
import subprocess
import speech_recognition as sr
from pytube import YouTube
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


def mp3_convert(videofile):
    while True:
        clip = VideoFileClip(videofile)
        clip.audio.write_audiofile("video.mp3")
        del clip.reader
        del clip
        break


def wav_convert():
    subprocess.call(['ffmpeg', '-i', 'video.mp3',
                'videoaudio.wav'])
    return


def downyoutu(url):
    youtube = YouTube(url)
    audio = youtube.streams.get_lowest_resolution()
    audio.download(filename='video.mp4')
    return


def get_large_audio_transcription(path, var):
    r = sr.Recognizer()
    """
    dividindo o audio em pequenos audios
    """
    # abrindo o arquivo de audio
    sound = AudioSegment.from_wav(path)  
    # dividindo o audio em pequenos pedacos baseado no silencio
    chunks = split_on_silence(sound,
        # mudar esse valor dependendo do arquivo
        min_silence_len = 500,
        # mudar esse valor dependendo do arquivo
        silence_thresh = sound.dBFS-14,
        # ficar em silencio mudar esse valor dependendo do arquivo
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # criando uma pasta para guardar os pedacos do audio
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    todo_texto = ""
    # processando cada pedaco 
    for i, audio_chunk in enumerate(chunks, start=1):
        # exportando os pedacos
        
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # reconhecendo os pedacos de audio
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # tentando converter pra texto
            try:
                text = r.recognize_google(audio_listened, language=var)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                todo_texto += text
   
    # retornando o texto 
    return todo_texto
  

if __name__ == '__main__':
    print('pagina de downloads')
