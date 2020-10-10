import tweepy
import pafy
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 20
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 40
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 40
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 40
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="DOWNLOAD MÚSICAS YOUTUBE")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="INSIRA O URL DO VÍDEO", font=self.fontePadrao)
        self.nomeLabel.pack(side=BOTTOM)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 60
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Baixar vídeo"
        self.autenticar["font"] = ("Arial", "12")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaURL
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def verificaURL(self):
        try:
            url = self.nome.get()
            video = pafy.new(url)
            allstreams = video.allstreams
            bestaudio = video.getbestaudio()
            tituloVideo = video.title
            filename = bestaudio.download(filepath=f"D:\Downloads\Vídeos\{tituloVideo}.mp3", meta=True, quiet=False)
            print(f"audio")
        except OSError:
            self.erroLabel = Label(self.quintoContainer, text="VERIFIQUE A PASTA DE INSTALAÇÃO", font=self.fontePadrao)
            self.erroLabel.pack(side=LEFT)
            print("da nao")

root = Tk()
Application(root)
root.mainloop()
