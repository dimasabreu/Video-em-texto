import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Checkbutton, Entry, StringVar, messagebox, filedialog
from conversor import *
import os
import shutil

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
logo = Image.open('images/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.place(relx=0.5, rely=0.08, anchor=tk.CENTER)


# instrucoes
instructions = tk.Label(root, text="Escolha um video do YouTube para extrair tudo que foi dito", font="Raleway")
instructions.place(relx=0.5, rely=0.18, anchor=tk.CENTER)
# criando um lugar para entrada de dados
e = Entry(root, width=70, borderwidth=3)
e.place(relx=0.5, rely=0.22, anchor=tk.CENTER)
e.insert(0, "Cole a URL")
content = ""


def open_file():
    botao_text.set("loading...")
    url = e.get()
    downyoutu(url)
    videofile = 'video.mp4'
    mp3_convert(videofile)
    wav_convert()
    global content
    print("comecando..")
    content = get_large_audio_transcription('videoaudio.wav', var.get())
    print("finalizado")
    text_box = tk.Text(root, height=22, width=74, padx=10, pady=15, font=("helvetica", 16), border=10, wrap='word')
    text_box.insert(1.0, content)
    text_box.tag_configure("left", justify="left")
    text_box.tag_add("center", 1.0, "end")
    text_box.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    botao_text.set("Enviar")
    return


def upload_file():
    global src
    upbutton_text.set("loading...")
    src = filedialog.asksaveasfilename()
    directory = os.getcwd()
    shutil.copy(src, directory)
    # diretorio
    path = directory
    # quantidade
    count = 1
    for f in os.scandir(path):
        if str(f.name).endswith('.mp4'):
            new_file = 'video'+'.mp4'
            src = os.path.join(path, f.name)
            dst = os.path.join(path, new_file)
            os.rename(src, dst)
            count += 1
    os.scandir(path).close()
    videofile = 'video.mp4'
    mp3_convert(videofile)
    wav_convert()
    global content
    content = get_large_audio_transcription('videoaudio.wav', var.get())
    text_box = tk.Text(root, height=22, width=74, padx=10, pady=15, font=("helvetica", 16), border=10, wrap='word')
    text_box.insert(1.0, content)
    text_box.tag_configure("left", justify="left")
    text_box.tag_add("center", 1.0, "end")
    text_box.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    upbutton_text.set("Enviar")
    return


def download_file():
    txt_text.set("Carregando...")
    file = open('videoemtexto.txt', 'w')
    file.write(content)
    file.close()
    txt_text.set("Baixado")
    return


# botao pra iniciar o download do video do yt
botao_text = tk.StringVar()
botao_btn = tk.Button(root, textvariable=botao_text, command=open_file, font="Raleway", bg="#20bebe", fg="white", height=2, width=15, border=3)
botao_text.set("Enviar")
botao_btn.place(relx=0.3, rely=0.28, anchor=tk.CENTER)

# botao do upload
upbutton_text = tk.StringVar()
upbutton_btn = tk.Button(root, textvariable=upbutton_text, command=upload_file, font="Raleway", bg="#20bebe", fg="white", height=2, width=15, border=3)
upbutton_text.set("Upload")
upbutton_btn.place(relx=0.5, rely=0.28, anchor=tk.CENTER)

# txt download button
txt_text = tk.StringVar()
txt_btn = tk.Button(root, textvariable=txt_text, command=download_file, font="Raleway", bg="#be2020", fg="black", height=2, width=15, border=3)
txt_text.set("Baixar o texto")
txt_btn.place(relx=0.7, rely=0.28, anchor=tk.CENTER)

# botao de checagem de linguas
var = StringVar()
lan_button = Checkbutton(root, text="Portugues", variable=var, onvalue='pt-br', offvalue='')
lan_button.place(relx=0.85, rely=0.15, anchor=tk.CENTER)
lan_button.deselect()


def on_closing():
    if messagebox.askokcancel("Fechar", "Você quer sair?"):
        root.destroy()
        if os.path.exists('video.mp3'):
            os.remove('video.mp3')
        if os.path.exists('videoaudio.wav'):
            os.remove('videoaudio.wav')
        if os.path.exists('video.mp4'):
            os.remove('video.mp4')
        if os.path.exists('audio-chunks'):
            shutil.rmtree('audio-chunks')
        if os.path.exists('videoemtexto2.txt'):
            os.remove('videoemtexto2.txt')


root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
