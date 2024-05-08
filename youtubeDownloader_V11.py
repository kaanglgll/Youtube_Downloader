import tkinter
import customtkinter
from pytube import YouTube

def Voice_Start_Download():
    try:
        YTlink = link.get()
        YTobject = YouTube(YTlink, on_progress_callback=on_progress)
        video = YTobject.streams.get_audio_only()
        video.download()
        title.configure(text=YTobject.title, text_color="white")
        finishLabel.configure(text="Indirme Tamamlandi!", text_color="red")
    except:
        finishLabel.configure(text="Duzgun link girin, Kedileri Uzmeyin!", text_color="red")


def Highq_Start_Download():
    try:
        YTlink = link.get()
        YTobject = YouTube(YTlink, on_progress_callback=on_progress)
        video = YTobject.streams.get_highest_resolution()
        video.download()
        title.configure(text=YTobject.title, text_color="white")
        finishLabel.configure(text="Indirme Tamamlandi!", text_color="red")
    except:
        finishLabel.configure(text="Duzgun link girin, Kedileri Uzmeyin!", text_color="red")


def Lowq_Start_Download():
    try:
        YTlink = link.get()
        YTobject = YouTube(YTlink, on_progress_callback=on_progress)
        video = YTobject.streams.get_lowest_resolution()
        video.download()
        title.configure(text=YTobject.title, text_color="white")
        finishLabel.configure(text="Indirme Tamamlandi!", text_color="red")
    except:
        finishLabel.configure(text="Duzgun link girin, Kedileri Uzmeyin!", text_color="red")
    

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text="%" + per)
    pPercentage.update()

    # Update Progress Bar
    progressBar.set(float(percentage_of_compeletion)/100)


# System settings
customtkinter.set_appearance_mode("system")     
customtkinter.set_default_color_theme("blue")


# app frame
app = customtkinter.CTk()
app.geometry("600x400")         # uygulama cercevesi boyutu
app.title("YOUTUBE VİDEO İNDİRİCİ") # uygulama basligi


# adding UI elements
title = customtkinter.CTkLabel(app, text="Bir YouTube linki giriniz.")
title.pack(padx=20, pady=25) # title uygulammadaki yerlesimi.


# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=35, textvariable=url_var)
link.pack()


# finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()


# progress percentage
pPercentage = customtkinter.CTkLabel(app, text="% 0")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# download buttons
ses_indirme_butonu = customtkinter.CTkButton(app, text="SES INDIR", command=Voice_Start_Download)
ses_indirme_butonu.pack(padx=10, pady=10)

ses_indirme_butonu = customtkinter.CTkButton(app, text="YUKSEK KALITE INDIR", command=Highq_Start_Download)
ses_indirme_butonu.pack(padx=10, pady=10)

ses_indirme_butonu = customtkinter.CTkButton(app, text="DUSUK KALITE INDIR", command=Lowq_Start_Download)
ses_indirme_butonu.pack(padx=10, pady=10)


# run app
app.mainloop() # uygulamanın hep acik kalmasini sagliyor.