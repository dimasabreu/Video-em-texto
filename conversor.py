from moviepy.editor import *
import subprocess
import speech_recognition as sr


def mp3_convert():
    i=0
    while i < 200:
        i += 1
    file = 'video.mp4'
    video = VideoFileClip(file)
    video.audio.write_audiofile("video.mp3")        
    return


def wav_convert():
    i=0
    while i < 200:
        i += 1
    subprocess.call(['ffmpeg', '-i', 'video.mp3', 
                'videoaudio.wav'])
    return


def text_convert():
    filename = "videoaudio.wav"
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
    return


if __name__ == '__main__':
    print('pagina de downloads')
