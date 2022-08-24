from moviepy.editor import *
import subprocess
import speech_recognition as sr
from pytube import YouTube
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


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

'''
def text_convert():
    filename = "videoaudio.wav"
    r = sr.Recognizer()
    # abrindo o arquivo
    with sr.AudioFile(filename) as source:
        audio = r.listen(source, phrase_time_limit=None)
        try:
            text = r.recognize_google(audio)
            print('Reconhecendo')
            return text
        except:
            print("deu erro")
    return
'''

def downyoutu(url):
    youtube = YouTube(url)
    audio = youtube.streams.get_lowest_resolution()
    audio.download(filename='video.mp4')
    return


def get_large_audio_transcription(path):
    r = sr.Recognizer()
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the ’folder_name’ directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                whole_text += text
                file = open('videoemtexto2.txt', 'w')
                file.write(whole_text)
                file.close()
                
    # return the text for all chunks detected
    return whole_text
  

if __name__ == '__main__':
    print('pagina de downloads')
