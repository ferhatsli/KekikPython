#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import telebot
import requests

# / Telegram Bağlantısı ################################################
Bot_Token = "XXXXXXXX:XXXXXXXXXX"                           # Bot Token
Chat_ID = "XXXXXXXXX"                                       # Chat ID

KekikPython = telebot.TeleBot(Bot_Token)  # telebot'a Tokenimizi bağladık
# / Telegram Bağlantısı ################################################

####################################################################################################################
# TeleBot Kütüphanesi ile Mesaj Gönderme
KekikPython.send_message(Chat_ID, "Merhaba, Beni TeleBot Gönderdi!")

# requests ile Mesaj Gönderme
gonderilecekYazi = "Merhaba, Beni requests Gönderdi!"
DataForLink = {'text': gonderilecekYazi}
requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendMessage?chat_id=" + Chat_ID , data=DataForLink)

# requests ile Dosya Gönderme
Dosya = open(r"C:\Users\kekik\Desktop\KekikAkademi.txt", 'rb')
FilesForLink = {'document': Dosya}
requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendDocument?chat_id=" + Chat_ID , files=FilesForLink)
####################################################################################################################

@KekikPython.message_handler(commands=['yardim', 'basla'])
def Yardim(Mesaj):
	KekikPython.reply_to(Mesaj, "İşte geldim burdayım !")

@KekikPython.message_handler(commands=['ls', 'list'])
def ls(Mesaj):
	KekikPython.reply_to(Mesaj, str(os.listdir(".")))

KekikPython.polling() # Aktif Bot

# https://pypi.org/project/pyTelegramBotAPI/