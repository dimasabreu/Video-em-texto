import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Entry, messagebox
from pytube import YouTube
from conversor import *
import os

root = tk.Tk()
root.title('Videos em texto')

# tamanho do monitor que acessou o programa
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# tamanho da tela do app
app_width = int(screen_width / 2)
app_height = int(screen_height / 1.2)

# pegando o ponto da tela pra por o app
x = (screen_width / 2) - (app_width / 2) 
y = (screen_height / 2) - (app_height / 2)
# parte de geometria q determina onde o app aparece na tela do usuario
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# tela do app
canvas = tk.Canvas(root, width=app_width, height=app_height)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.place(relx=0.5, rely=0.08, anchor=tk.CENTER)


# instrucoes
instructions = tk.Label(root, text="Escolha um video do YouTube em INGLES para extrair tudo que foi dito", font="Raleway")
instructions.place(relx=0.5, rely=0.18, anchor=tk.CENTER)
# criando um lugar para entrada de dados
e = Entry(root, width=70, borderwidth=3)
e.place(relx=0.5, rely=0.22, anchor=tk.CENTER)
e.insert(0, "Cole a URL")
content = ""


def open_file():
    botao_text.set("loading...")
    url = e.get()
    youtube = YouTube(url)
    audio = youtube.streams.get_lowest_resolution()
    audio.download(filename='video.mp4')
    mp3_convert()
    wav_convert()
    text_convert()
    global content
    content = text_convert()
    text_box = tk.Text(root, height=22, width=74, padx=10, pady=15, font=("Helvetiva", 16), border=10)
    text_box.insert(1.0, content)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    botao_text.set("Enviar")
    return


# botao basico
botao_text = tk.StringVar()
botao_btn = tk.Button(root, textvariable=botao_text, command=open_file, font="Raleway", bg="#20bebe", fg="white", height=2, width=15, border=3)
botao_text.set("Enviar")
botao_btn.place(relx=0.4, rely=0.28, anchor=tk.CENTER)


def download_file():
    txt_text.set("Carregando...")
    file = open('videoemtexto.txt', 'w')
    file.write(content)
    file.close()
    txt_text.set("Download finalizado")
    return

# txt button
txt_text = tk.StringVar()
txt_btn = tk.Button(root, textvariable=txt_text, command=download_file, font="Raleway", bg="#be2020", fg="white", height=2, width=15, border=3)
txt_text.set("Baixar o texto")
txt_btn.place(relx=0.6, rely=0.28, anchor=tk.CENTER)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        os.remove('video.mp3')
        os.remove('videoaudio.wav')


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
