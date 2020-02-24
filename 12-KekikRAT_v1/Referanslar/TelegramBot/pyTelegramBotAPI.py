#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import requests
import telebot

# / Telegram Bağlantısı ################################################
Bot_Token = "XXXXXXXX:XXXXXXXXXX"                           # Bot Token
Chat_ID = "XXXXXXXXX"                                       # Chat ID

KekikPython = telebot.TeleBot(Bot_Token)  # telebot'a Tokenimizi bağladık
# / Telegram Bağlantısı ################################################

####################################################################################################################
### Eski Usul requests Metodu;
# requests ile Mesaj Gönderme --- https://core.telegram.org/bots/api
Mesaj = "Merhaba, Beni requests Gönderdi!"
DataForLink = {'text': Mesaj}
requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendMessage?chat_id=" + Chat_ID , data=DataForLink)

# requests ile Dosya Gönderme
Dosya = open(r"DocTest_KekikAkademi.txt", 'rb') # veya "C:\Users\kekik\Desktop\kodlama\DocTest_KekikAkademi.txt"
FilesForLink = {'document': Dosya}
requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendDocument?chat_id=" + Chat_ID , files=FilesForLink)

# requests ile Resim Gönderme
# (Eğer Fotoğrafta Çözünürlük Kaybı Yaşanmasını İstemiyorsanız Dosya Olarak Gönderin.)
Resim = open(r"FotoTest_KekikAkademi.png", 'rb') # veya "C:\Users\kekik\Desktop\kodlama\FotoTest_KekikAkademi.png"
ImgForLink = {'photo': Resim}
requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendPhoto?chat_id=" + Chat_ID , files=ImgForLink)

#####################################################################
### Yeni Nesil TeleBot Metodu;
# TeleBot ile Mesaj Gönderme --- https://github.com/eternnoir/pyTelegramBotAPI#telebot
Mesaj = "Merhaba, Beni TeleBot Gönderdi!"
KekikPython.send_message(Chat_ID, Mesaj)

# TeleBot ile Dosya Gönderme
Dosya = open(r"DocTest_KekikAkademi.txt", 'rb') # veya "C:\Users\kekik\Desktop\kodlama\DocTest_KekikAkademi.txt"
KekikPython.send_document(Chat_ID, Dosya)

# TeleBot ile Resim Gönderme
# (Eğer Fotoğrafta Çözünürlük Kaybı Yaşanmasını İstemiyorsanız Dosya Olarak Gönderin.)
Resim = open(r"FotoTest_KekikAkademi.png", 'rb') # veya "C:\Users\kekik\Desktop\kodlama\FotoTest_KekikAkademi.png"
KekikPython.send_photo(Chat_ID, Resim)
####################################################################################################################

@KekikPython.message_handler(commands=['yardim', 'basla'])
def Yardim(Mesaj):
	KekikPython.reply_to(Mesaj, "İşte geldim burdayım !")

@KekikPython.message_handler(commands=['ls', 'list'])
def ls(Mesaj):
	KekikPython.reply_to(Mesaj, str(os.listdir(".")))

KekikPython.polling() # Aktif Bot