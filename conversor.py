from moviepy.editor import *
import subprocess
import speech_recognition as sr
from pytube import YouTube


def mp3_convert():
    while True:
        clip = VideoFileClip('video.mp4')
        clip.audio.write_audiofile("video.mp3")
        del clip.reader
        del clip
        break


def wav_convert():
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


def downyoutu(url):
    youtube = YouTube(url)
    audio = youtube.streams.get_lowest_resolution()
    audio.download(filename='video.mp4')
    return


if __name__ == '__main__':
    print('pagina de downloads')
