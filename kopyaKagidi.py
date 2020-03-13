#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

########################################################################################################################
## ModulYukle
# https://github.com/raif-py/pentester/blob/master/PentesterBeta.py
import os                       # Dizinler ve dosyalarla çalışmak için
import platform                 # Çalışılan makine bilgisi sağlayacak arkadaş
#############################################
try:                                        # Dene
    import time,datetime,pytz               # Zaman/Tarih Bilgisi sağlayacak arkadaşları eklemeyi
except ModuleNotFoundError:                 # Modül Bulunamadı Hatası Alırsan
    print("\n\tEksik modüllerin varmış,\n\t\tSenin için pip3 ile yüklemeyi deniyorum..")
    if platform.system() == "Windows":      # Eğer İşletim Sistemi Windows İse
        os.system("pip install time")       # pip ile Yükle
        os.system("pip install datetime")   # pip ile Yükle
        os.system("pip install pytz")       # pip ile Yükle
    else:                                   # İşletim Sistemi Windows Değilse
        os.system("pip3 install time")      # pip3 ile Yükle
        os.system("pip3 install datetime")  # pip3 ile Yükle
        os.system("pip3 install pytz")      # pip3 ile Yükle
    import time, datetime, pytz             # Zaman/Tarih Bilgisi sağlayacak arkadaşları ekle
#############################################
try:                                        # Dene
    import requests                         # ip bilgisi almak için websitesine istek atıcak arkadaşı eklemeyi
except ModuleNotFoundError:                 # Modül Bulunamadı Hatası Alırsan
    print("\n\tEksik modüllerin varmış,\n\t\tSenin için pip3 ile yüklemeyi deniyorum..")
    if platform.system() == "Windows":      # Eğer İşletim Sistemi Windows İse
        os.system("pip install requests")   # pip ile Yükle
    else:                                   # İşletim Sistemi Windows Değilse
        os.system("pip3 install requests")  # pip3 ile Yükle
    import requests                         # ip bilgisi almak için websitesine istek atıcak arkadaşı ekle
#############################################
try:                                        # Dene
    import ctypes                           # C dili veri tipleri kullanmamızı sağlayacak arkadaşı eklemeyi (.DLL / .SO)
except ModuleNotFoundError:                 # Modül Bulunamadı Hatası Alırsan
    print("\n\tEksik modüllerin varmış,\n\t\tSenin için pip3 ile yüklemeyi deniyorum..")
    if platform.system() == "Windows":      # Eğer İşletim Sistemi Windows İse
        os.system("pip install ctypes")     # pip ile Yükle
    else:                                   # İşletim Sistemi Windows Değilse
        os.system("pip3 install ctypes")    # pip3 ile Yükle
    import ctypes                           # C dili veri tipleri kullanmamızı sağlayacak arkadaşı ekle (.DLL / .SO)
#############################################
try:                                        # Dene
    import colorama                         # Ortalığın renklenmesini sağlayacak arkadaşı eklemeyi
except ModuleNotFoundError:                 # Modül Bulunamadı Hatası Alırsan
    print("\n\tEksik modüllerin varmış,\n\t\tSenin için pip3 ile yüklemeyi deniyorum..")
    if platform.system() == "Windows":      # Eğer İşletim Sistemi Windows İse
        os.system("pip install colorama")   # pip ile Yükle
    else:                                   # İşletim Sistemi Windows Değilse
        os.system("pip3 install colorama")  # pip3 ile Yükle
    import colorama                         # Ortalığın renklenmesini sağlayacak arkadaşı ekle
#############################################
from colorama import Fore       # Boyamayı kolaylaştıran arkadaş (BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE)
colorama.init(autoreset=True)   # Renklerin ilgili satırdan başka satıra devam etmemesi için
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
    kullanici_adi = os.getlogin()                                               # Kullanıcı Adı
except:
    import pwd
    kullanici_adi = pwd.getpwuid(os.geteuid())[0]                               # Kullanıcı Adı
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

ust_bilgi = f"""
    {Fore.LIGHTBLACK_EX}{kullanici_adi} | {cihaz} | {Fore.LIGHTGREEN_EX}{ip} 
          {Fore.YELLOW}{zaman}
    """                                                                         # Üst Bilgimiz
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
def PencereBasligi():                                                   # PencereBasligi fonksiyonu
    if isletim_sistemi == "Windows":                                    # Eğer İşletim Sistemi "Windows" ise
        ctypes.windll.kernel32.SetConsoleTitleW(f"{pencere_basligi}")   # Konsol Başlığını ayarla
    elif isletim_sistemi == "Android":                                  # Eğer İşletim Sistemi "Android" ise
        os.system("clear")                                              # Sisteme "clear" komutu gönder
    elif isletim_sistemi == "Linux":                                    # Eğer İşletim Sistemi "Linux" ise
        os.system(f'echo "\033]0;{pencere_basligi}\007"')               # Başlık Ayarla
    else:                                                               # Hiçbiri değil ise
        os.system(f'title {pencere_basligi}')                           # Başlık Ayarla
PencereBasligi()    # PencereBasligi çağır
########################################################################################################################

########################################################################################################################
def WindowsBildirimi():                         # WindowsBildirimi adında bir metod oluşturduk
    if isletim_sistemi == "Windows":            # Eğer İşletim Sistemi "Windows" ise
        from win10toast import ToastNotifier    # Windows'a bildirim göndermek için
        bildirim = ToastNotifier()
        bildirim.show_toast("Bildirim Gibi Bildirim", "Kopya Kağıdı", icon_path=None, duration=10, threaded=True)
    else:                                       # Eğer İşletim Sistemi "Windows" değilse
        pass                                    # Boşver
WindowsBildirimi()
########################################################################################################################

######################################## Her Şey Burda Başlar :) #######################################################

########################################################################################################################
def  ProgressBar():
    ### Modül Yükle #####################################################
    try:
        from tqdm import tqdm
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install tqdm")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install tqdm")  # pip3 ile Yükle
        from tqdm import tqdm
    ######################################################################
    try:
        from time import sleep
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install time")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install time")  # pip3 ile Yükle
        from time import sleep
    ######################################################################
    try:
        from random import uniform
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install random")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install random")  # pip3 ile Yükle
        from random import uniform
    ### / Modül Yükle #####################################################
    Temizle()

    for i in tqdm(range(10)):
        sleep(0.2)

    pbar = tqdm(["a", "b", "c", "d", "e", "f", "g", "h", "j", "k"])
    for i in pbar:
        pbar.set_description(f'Processing >> {i}')
        sleep(0.3)

    for i in tqdm(range(100), unit=" keystrokes", desc="Loading ", position=1):
        sleep(uniform(0.001, 0.03))
########################################################################################################################

########################################################################################################################
def YoutubeScraper(): # https://www.instagram.com/p/B7RGVGqgQBO/
    ### Modül Yükle #####################################################
    try:
        import requests
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install requests")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install requests")  # pip3 ile Yükle
        import requests
    ######################################################################
    try:
        from bs4 import BeautifulSoup
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install bs4")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install bs4")  # pip3 ile Yükle
        from bs4 import BeautifulSoup
    ### / Modül Yükle #####################################################
    Temizle()

    def Scrape(link):
        data = []                   # Gelecek datalar için boş liste oluşturduk
        link = link + '/videos'     # Vidyolara gidiyoruz
        r = requests.get(link)      # link'e İstek yolluyoruz
        s = BeautifulSoup(r.text,"html5lib")    # Suop objemiz

        for i in s.find_all('h3', class_="yt-lockup-title")[:15]:   # 15 Vidyo tara
            title = i.a.attrs['title']                              # Başlığı ayıkla
            v_link = i.a.attrs['href']                              # Linki Ayıkla
            v_link = f"https://youtube.com{v_link}"                 # Linki ver
            print(f"Başlık : {title}\nLink : {v_link}\n{'*' * 75}") # Ekrana yaz
            data.append((title, v_link))                            # dataya ekle

        return data     # data'ya dön

    link = input("Youtube Kullanıcı Adı Girin : ")
    link = f"https://youtube.com/{link}"        # link tanımlaması
    data = Scrape(link)                         # data tanımlaması
    print(f"Datalar;\n{data}")                  # ekrana datayı yaz
########################################################################################################################

########################################################################################################################
def InstagramScraper(): # https://www.instagram.com/p/B7Lv_HaAIWY/
    ### Modül Yükle #####################################################
    try:
        import requests
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install requests")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install requests")  # pip3 ile Yükle
        import requests
    ######################################################################
    try:
        from bs4 import BeautifulSoup
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install bs4")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install bs4")  # pip3 ile Yükle
        from bs4 import BeautifulSoup
    ### / Modül Yükle #####################################################
    Temizle()

    url = "https://instagram.com/{}/"

    def Scrape(username):
        full_url = url.format(username)
        r = requests.get(full_url)
        s = BeautifulSoup(r.text, "html5lib")

        tag = s.find("meta", attrs = {"name":"description"})
        text = tag.attrs['content']
        main_text = text.split("-")[0]

        return main_text

    username = input("Instagram Kullanıcı Adı Girin : ")
    username = f"{username}"
    data = Scrape(username)
    print(data)
########################################################################################################################

########################################################################################################################
def ProxyCrawler(): # https://www.instagram.com/p/B7JOl9iA1h4/
    ### Modül Yükle #####################################################
    try:
        import requests
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install requests")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install requests")  # pip3 ile Yükle
        import requests
    ######################################################################
    try:
        from bs4 import BeautifulSoup
    except ModuleNotFoundError:
        if platform.system() == "Windows":  # Eğer İşletim Sistemi Windows İse
            os.system("pip install bs4")  # pip ile Yükle
        else:  # İşletim Sistemi Windows Değilse
            os.system("pip3 install bs4")  # pip3 ile Yükle
        from bs4 import BeautifulSoup
    ### / Modül Yükle #####################################################
    Temizle()

    def CrawlProxies():
        proxies = []
        link = "https://sslproxies.org"

        r = requests.get(link)
        s = BeautifulSoup(r.text, "html5lib")

        for i in s.find_all("tr")[0:30]:
            try:
                data = i.find_all("td")
                adress = data[0].text
                port = data[1].text
                type_ = data[4].text
                proxy = f"{adress}:{port}"
                print(f"https : {proxy}\n{'*' * 35}")  # Ekrana yaz
                proxies.append({"https":proxy})
            except:
                pass
        return proxies

    proxies = CrawlProxies()
    print(f"Proxyler ;\n{proxies}")                  # ekrana datayı yaz
########################################################################################################################

########################################################################################################################
def AcilisSayfasi():
    Temizle()
    print(Fore.GREEN + logo)        # yeşil renk koduyla logomuzu yazdırdık
    print(ust_bilgi)                # Üst Bilgimizi yazdırdık
    print(f"""
    {Fore.GREEN}[{Fore.YELLOW} 1 {Fore.GREEN}] {Fore.CYAN}Progress Bar
    {Fore.GREEN}[{Fore.YELLOW} 2 {Fore.GREEN}] {Fore.CYAN}Youtube Scraper
    {Fore.GREEN}[{Fore.YELLOW} 3 {Fore.GREEN}] {Fore.CYAN}Instagram Scraper
    {Fore.GREEN}[{Fore.YELLOW} 4 {Fore.GREEN}] {Fore.CYAN}Proxy Crawler
    """) # Seçeneklerimizi ayarladık

    konum = os.getcwd()
    if isletim_sistemi == "Windows":
        konum = konum.split("\\")
    elif isletim_sistemi == "Linux":
        konum = konum.split("/")
    else:
        konum = "/"
    secenek = str(input(
        f"{Fore.RED}{oturum}:{Fore.LIGHTBLUE_EX}~/../{konum[-2] + '/' + konum[-1]} >> {Fore.GREEN}")
        ) # Kullanıcı için input oluşturduk
    ###########################################################################
    if secenek == '1' or secenek == '01':      # Eğer 1 i seçerse
        Temizle()
        ProgressBar()
    ###########################################################################
    elif secenek == '2' or secenek == '02':    # Eğer 2 yi seçerse
        Temizle()
        YoutubeScraper()
    ###########################################################################
    elif secenek == '3' or secenek == '03':    # Eğer 3 ü seçerse
        Temizle()
        InstagramScraper()
    ###########################################################################
    elif secenek == '4' or secenek == '04':    # Eğer 4 ü seçerse
        Temizle()
        ProxyCrawler()
    ###########################################################################
    else:                   # Eğer harici bişey seçerse
        pass                # Aldırış etme (çökme)
        Temizle()           # Temizle fonksiyonunu çalıştır
        AcilisSayfasi()     # AcilisSayfasi fonksiyonunu çalıştır
########################################################################################################################

AcilisSayfasi()