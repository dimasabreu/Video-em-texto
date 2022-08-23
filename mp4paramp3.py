from moviepy.editor import *
import glob
import subprocess
import speech_recognition as sr


def mp3_convert():
    i=0
    while i < 200:
        i += 1
    for file in glob.glob("*.mp4"):
        video = VideoFileClip(file)
        video.audio.write_audiofile("video.mp3")        


def wav_convert():
    i=0
    while i < 200:
        i += 1
    subprocess.call(['ffmpeg', '-i', 'video.mp3', 
                'arquivodeaudio.wav'])


def text_convert():
    filename = "arquivodeaudio.wav"
    r = sr.Recognizer()
    # abrindo o arquivo
    with sr.AudioFile(filename) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('Reconhecendo')
            return text
        except:
            print("deu erro")
