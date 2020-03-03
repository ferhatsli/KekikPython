#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

########################################################################################################################
## https://github.com/KekikAkademi/KekikPython/blob/master/11-KekikTelegram/KekikTelegram.py
import os                       # Dizinler ve dosyalarla çalışmak için
import platform                 # Çalışılan makine bilgisi sağlayacak arkadaş
import time,datetime,pytz       # Zaman/Tarih Bilgisi sağlayacak arkadaşlar
import ctypes                   # C dili veri tipleri kullanmamızı sağlayacak arkadaş (.DLL / .SO)
import colorama                 # Ortalığın renklenmesini sağlayacak arkadaş
from colorama import Fore       # Boyamayı kolaylaştıran arkadaş (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
colorama.init(autoreset=True)        # Renklerin ilgili satırdan başka satıra devam etmemesi için
######################################
## https://github.com/KekikAkademi/KekikPython/tree/master/8-KekikDoviz
import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş
from bs4 import BeautifulSoup   # HTML veya XML dosyalarını işleyen arkadaş
#################################
import telebot    # pyTelegramBotAPI
####################################
#############################################################################################################
## https://github.com/KekikAkademi/KekikPython/tree/master/12-KekikRAT_v1                                   #
#import webbrowser           # Tarayıcıda bağlantı açtırmak için                                            #
#import subprocess           # Kill Process(İşlem Sonlandırma) Kullanmak için                               #
#import shutil               # Tarayıcı verilerini kopyalamak için                                          #
#import sqlite3              # Tarayıcıdan çekilen veritabanlarıyla çalışmak için                           #
#import win32crypt           # Tarayıcıdan çekilen şifrelenmiş verileri çözmek için (Yalnızca Windows)      #
#from PIL import ImageGrab   # Ekran görüntüsü almak için (MacOS ve Windows)                                #
#import zipfile              # Topladığımız verileri Zip'lemek için                                         #
#############################################################################################################
def ModulYukle(): # https://github.com/KekikAkademi/KekikPython/blob/master/7-Kekik-File-Stealer/Renkli.py
    try:                                    # Dene
        import requests                     # requests Modülünü içe Aktarmayı
    except ModuleNotFoundError:             # Modül bulunamadıysa
        os.system("pip3 install requests")  # Yükle
        try:                                # Dene
            import requests                 # requests Modülünü içe Aktarmayı
        except Exception as hata:           # Hala hata var ise
            sys.exit(f"{Fore.RED}requests yüklenemedi !\n\n{Fore.CYAN}Log : {Fore.LIGHTBLACK_EX}{hata}") # Kapat(yazdır)
    except:
        pass                                # Olmuyosa zorlamayacaksın :)
#ModulYukle()
########################################################################################################################

########################################################################################################################
## GenelDegiskenler
pencere_basligi = "@KekikAkademi Kopya Kağıdı"                        # Pencere Başlığımız
logo = '''
 _                             _   __            _     _ _ 
| |                           | | / /           (_)   | (_)
| | _____  _ __  _   _  __ _  | |/ /  __ _  __ _ _  __| |_ 
| |/ / _ \| '_ \| | | |/ _` | |    \ / _` |/ _` | |/ _` | |
|   < (_) | |_) | |_| | (_| | | |\  \ (_| | (_| | | (_| | |
|_|\_\___/| .__/ \__, |\__,_| \_| \_/\__,_|\__, |_|\__,_|_|
          | |     __/ |                     __/ |          
          |_|    |___/                     |___/           
'''                                                                   # Logomuz
        # logo = http://patorjk.com/software/taag/#p=display&f=Doom&t=kopya%20Kagidi
#######################################################################################
try:
    kullanici_adi = os.getlogin()                                     # Kullanıcı Adı
except:
    import pwd
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]                     # Kullanıcı Adı
bilgisayar_adi = platform.node()                                      # Bilgisayar Adı
oturum = kullanici_adi + "@" + bilgisayar_adi                         # Örn.: "kekik@Administrator"

isletim_sistemi = platform.system()                                             # İşletim Sistemi
bellenim_surumu = platform.release()                                            # Sistem Bellenim Sürümü
cihaz = isletim_sistemi + " | " + bellenim_surumu                               # Örn.: "Windows | 10"

tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")     # Bugünün Tarihi
saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M")         # Bugünün Saati
zaman = tarih + " | " + saat

ip_req = requests.get('http://ip.42.pl/raw')    # Harici IP'yi bulmak için bir GET isteği yolluyoruz
ip = ip_req.text                                # ip Adresi

ust_bilgi = f"""
    {Fore.LIGHTBLACK_EX}{kullanici_adi} | {cihaz} | {Fore.LIGHTGREEN_EX}{ip} 
          {Fore.YELLOW}{zaman}
    """                                                               # Üst Bilgimiz
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
        ctypes.windll.kernel32.SetConsoleTitleW(f"{pencere_basligi}")       # Konsol Başlığını ayarla
    elif isletim_sistemi == "Android":                                              # Eğer İşletim Sistemi "Android" ise
        os.system("clear")                                                          # Sisteme "clear" komutu gönder
    elif isletim_sistemi == "Linux":                                                # Eğer İşletim Sistemi "Linux" ise
        os.system(f'echo "\033]0;{pencere_basligi}\007"')                   # Başlık Ayarla
    else:                                                                           # Hiçbiri değil ise
        os.system(f'title {pencere_basligi}')                               # Başlık Ayarla
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
def  WebCrawl():
    # Tanımlamalarımızı Yapalım
    url = "https://www.doviz.com/"
    kimlik = {'User-Agent': '@KekikAkademi'} # Websitesine istek yollarken kimlik bilgimizi sunuyoruz

    # WebSitesinin Cevabına bakalım (ilk kontrol)
    #cevap = requests.get(url, headers=kimlik)
    #print(cevap)

    # Sorun yoksa devam edelim
    kaynak = requests.get(url, headers=kimlik).text # Url'nin içerisindeki bütün html dosyasını indiriyoruz.
    sayfa_oku = BeautifulSoup(kaynak , "html.parser")
    #print(sayfa_oku)                               # bakalım bize gelen veri görüntülenen ile aynı mı?(ikinci kontrol)

    # Siteye girdik. Ne Alıcaz Burdan?
    isim = []       # içerisine veri ekleyeceğimiz boş tablo
    rakam = []      # içerisine veri ekleyeceğimiz boş tablo
    oran = []       # içerisine veri ekleyeceğimiz boş tablo

    # Hadi Kazıyalım!
    for ayristirilan_alan in sayfa_oku.findAll('div', attrs={'class':'market-data'}):
        #print(ayristirilan_alan)       # ilk ayrıştırmamızı yaptık
        #print(ayristirilan_alan.text)  # Bir de kodlardan arındırıp bakalım

        # Parçalamaya devam edelim
        for birinci in ayristirilan_alan.findAll('span', attrs={'class':'name'}):
            #print(birinci)             # Bakalım ne geldi
            gelenisim = birinci.text    # kodlarından ayıralım
            #print(gelenisim)           # kontrol edelim, olmuşsa devam
            isim.append(gelenisim)      # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            #Tablo kontrolünü "print(isim)" döngünün dışında yapmayı unutma !

        # şimdi de rakamları çekelim
        for ikinci in ayristirilan_alan.findAll('span', attrs={'class':'value'}):
            #print(ikinci)              # Bakalım ne geldi
            gelenrakam = ikinci.text    # kodlarından ayıralım
            #print(gelenrakam)          # kontrol edelim, olmuşsa devam
            rakam.append(gelenrakam)    # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            ## Tablo kontrolünü "print(rakam)" döngünün dışında yapmayı unutma !

        # oranları da çekersek tamamdır
        for ucuncu in ayristirilan_alan.findAll('div', attrs={'class':'change'}):
            #print(ucuncu)                  # Bakalım ne geldi
            gelenoran = ucuncu.text         # kodlarından ayıralım
            #print(gelenoran)               # kontrol edelim, boşluklarımız var. boşlukları yok etmeliyiz..
            gelenoran = gelenoran.replace("\n", "") # boşlukları kaldır
            #print(gelenoran)                       # hala değil
            gelenoran = gelenoran.replace(" ", "")  # boşlıkları kaldır :)
            #print(gelenoran)                       # tamamdır :)
            oran.append(gelenoran)          # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            ## Tablo kontrolünü "print(oran)" döngünün dışında yapmayı unutma !

    # Tablolarımızı kontrol edelim
    #print(isim)
    #print(rakam)
    #print(oran)
    # haaarika
    for i in range(0, len(isim)):  # döngüyü isim tablosunun elemanı kadar sürdür
        print(Fore.MAGENTA + "*"*30 + "\n" +
              Fore.GREEN + f"{isim[i]} " + Fore.RED + ">>" +
              Fore.YELLOW + f" {rakam[i]} " + Fore.RED + ">>" +
              Fore.CYAN + f" {oran[i]}" +
              "\n" + Fore.MAGENTA + "*"*30)

    print("\n\t" + Fore.YELLOW + "Teşekkürler doviz.com")

    time.sleep(10)  # DDoS gibi olmaması için 10 saniye aralık la yap bu işi
    Temizle()       # Temizle metodumuzu çağırdık
#WebCrawl()
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
        # https://api.telegram.org/bot921015578:AAERTtQ-LxeG6huZZw-dbmW1LQjJv9yZK4Q/sendMessage?chat_id=717569643&text=mesaj

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
        dosya = open(r"DocTest_KekikAkademi.txt", 'rb') # veya "C:\Users\kekik\Desktop\DocTest_KekikAkademi.txt"
        tg_bot_adi.send_document(tg_chat_id, dosya)

        # TeleBot ile Resim Gönderme
        # (Eğer Fotoğrafta Çözünürlük Kaybı Yaşanmasını İstemiyorsanız Dosya Olarak Gönderin.)
        resim = open(r"FotoTest_KekikAkademi.png", 'rb') # veya "C:\Users\kekik\Desktop\FotoTest_KekikAkademi.png"
        tg_bot_adi.send_photo(tg_chat_id, resim)
        ##############################
    TelegramBotTest()
#TelegramBot()
########################################################################################################################

########################################################################################################################
def TelegramUdemy(): # @raifpy
    from bs4 import BeautifulSoup as bs

    tg_bot_token = "921015578:AAERTtQ-LxeG6huZZw-dbmW1LQjJv9yZK4Q" # Bot Token
    tg_chat_id = "717569643"                                       # Chat ID

    def mesaj(konu):
        requests.post(f"https://api.telegram.org/bot{tg_bot_token}/sendMessage",
                      data={"chat_id": f"{tg_chat_id}", "text": konu})

    def start(sayi):
        sayi = str(sayi)  # int olan değerimizi str yapıyoruz
        link = "http://www.discudemy.com/all/" + sayi  # sayfalar arasında gezinmek için
        kimlik = {'User-Agent': '@KekikAkademi'} # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
        html = requests.get(link, headers=kimlik) # Url'nin içerisindeki bütün html dosyasını indiriyoruz.
        kaynak = bs(html.text, "html.parser")  # bitifulsup ile html'i işlememiz gerekiyor . html.parser'i kullandık

        #######################################################################################
        linkler = kaynak.find_all("a", attrs={
            "class": "card-header"})  # sınıf'ı kart-header olan tüm linkleri çekiyoruz bununla
        #######################################################################################
        for i in linkler:       # linkler listesini i olarak ayırdık
            i = i["href"]       # i'nin hreflerini aldık (linkleri)
            i = i.split("/")    # discudemy.com/katagori olan linki udemy.com olarak değiştirmemiz gerekiyor.
                                # Bunun için / 'ları bulduktan sonra buralardan bölüyoruz
            i = i[0] + "//www.udemy.com/course/" + i[4]  # i[0] = https: i[4] = udemy linki'miz
            mesaj(i)            # i değerimizi (linkimizi) mesaj yolla kısmı ile telegramdan attık
            print(f"{Fore.LIGHTBLACK_EX}{i} {Fore.CYAN}| {Fore.GREEN} Gönderildi !") # i değerimizi (linkimizi) yazdık
        ##############################################################################################################

    mesaj(f"""Udemy kurs botu aktif !
Kaynak : discudemy.com
Teşekkürler : @KekikAkademi

Sunucu mimari : {platform.system()}
Sunucu : {platform.release()}

Lütfen geri bildirimde bulunun ..""")  # bot başladı mesajı atıyoruz
    ################################################################

    for ii in range(1, 400):    # Neden : discumdey.com sitesi site.com/all/1 ,2 ,4 ,200 şeklinde kursları yayınlıyor.
                                # Bu sepeten döngüne aldık . Elbette geliştirilebilir
        start(ii)               # start dediğimiz eleman herşeyi başlatan
        time.sleep(300)         # 5 dakika beklemesini sağlıyoruz

#TelegramUdemy()
########################################################################################################################

########################################################################################################################
def AcilisSayfasi():
    print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
    print(ust_bilgi)                # Üst Bilgimizi yazdırdık
    print(f"""
    {Fore.GREEN}[{Fore.YELLOW} 1 {Fore.GREEN}] {Fore.CYAN}WebCrawl Örneği
    {Fore.GREEN}[{Fore.YELLOW} 2 {Fore.GREEN}] {Fore.CYAN}TelegramBot Test
    {Fore.GREEN}[{Fore.YELLOW} 3 {Fore.GREEN}] {Fore.CYAN}TelegramUdemy
    """) # Seçeneklerimizi ayarladık

    secenek = str(input(f"{Fore.RED}{oturum}{Fore.LIGHTBLUE_EX} >> {Fore.GREEN}")) # Kullanıcı için input oluşturduk
    #########################
    if secenek == '1':      # Eğer 1 i seçerse
        Temizle()           # Temizle fonksiyonunu çalıştır
        while True:         # Sonsuz döngü başlat
            print(ust_bilgi)# Üst Bilgi fonksiyonunu çalıştır
            WebCrawl()      # WebCrawl fonksiyonunu çalıştır
    #########################
    elif secenek == '2':    # Eğer 2 yi seçerse
        Temizle()           # Temizle fonksiyonunu çalıştır
        print(ust_bilgi)    # Üst Bilgi fonksiyonunu çalıştır
        print("Telegram Bot Testi\n")
        TelegramBot()       # TelegramBot fonksiyonunu çalıştır
    #########################
    elif secenek == '3':    # Eğer 3 ü seçerse
        while True:         # Sonsuz döngü başlat
            Temizle()       # Temizle fonksiyonunu çalıştır
            print(ust_bilgi)# Üst Bilgi fonksiyonunu çalıştır
            print("Telegram Udemy Botu\n")
            TelegramUdemy()# TelegramUdemy fonksiyonunu çalıştır
    #########################
    else:                   # Eğer harici bişey seçerse
        pass                # Aldırış etme (çökme)
        Temizle()           # Temizle fonksiyonunu çalıştır
        AcilisSayfasi()     # AcilisSayfasi fonksiyonunu çalıştır

AcilisSayfasi()
########################################################################################################################