import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Entry
from pytube import YouTube
from mp4paramp3 import *

root = tk.Tk()
root.title('Videos em texto')

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


# instrucoes
instructions = tk.Label(root, text="Escolha um video do YouTube em EN para ver extrair tudo que foi dito", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)
# criando um lugar para entrada de dados
e = Entry(root, width=70, borderwidth=3)
e.grid(columnspan=3, column=0, row=2)
e.insert(0, "Cole a URL")
content = ""


def open_file():
    browse_text.set("loading...")
    url = e.get()
    youtube = YouTube(url)
    audio = youtube.streams.get_lowest_resolution()
    audio.download()
    mp3_convert()
    wav_convert()
    text_convert()
    global content
    content = text_convert()
    text_box = tk.Text(root, height=20, width=100, padx=15, pady=15, font=("Helvetiva", 16))
    text_box.insert(1.0, content)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=3)
    


# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=open_file, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Enviar")
browse_btn.grid(column=1, row=3)

canvas = tk.Canvas(root, width=0, height=50)
canvas.grid(columnspan=1)


def download_file():
    txt_text.set("loading...")
    file = open('videoemtexto.txt', 'w')
    file.write(content)
    file.close()
    txt_text.set("Baixar o texto")


# txt button
txt_text = tk.StringVar()
txt_btn = tk.Button(root, textvariable=txt_text, command=download_file, font="Raleway", bg="#be2020", fg="white", height=2, width=15)
txt_text.set("Baixar o texto")
txt_btn.grid(column=1, row=4)













root.mainloop()