#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import time,datetime,pytz,os,platform   # OturumBilgisi sağlayacak arkadaşlar
import requests                         # İstek gönderici arkadaşımız
from bs4 import BeautifulSoup           # Ayrıştırıcı arkadaşımız

##
# Önce çalışma alanımızı oluşturuyoruz
Sistem = platform.system() # Betiğin çalıştığı işletim sistemini öğreniyoruz

def Temizle(): # Temizle adında bir betik oluşturduk
    if Sistem == "Windows": # Eğer Sistem Windows ise
        os.system("cls") # Sisteme "cls" komutu gönder
    else: # Sistem Windows değil ise
        os.system("clear") # Sisteme "clear" komutu gönder
Temizle() # Temizle metodumuzu çağırdık

SistemKullaniciAdi = os.getlogin() # Sistem Kullanıcı Adı
Tarih = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y") # Bugünün Tarihini Alıyoruz
Saat = datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M") # Bugünün Saatini Alıyoruz

def OturumBilgisi(): # OturumBilgisi adında bir betik oluşturduk
    print("\n\t" + SistemKullaniciAdi  + "\t<<<< Oturum Bilgisi >>>>\t" + Tarih + "\t|\t" + Saat + "\n") # Anlık oturum ve tarh bilgisini ekranımıza yazıyoruz.
OturumBilgisi() # OturumBilgisi metodumuzu çağırdık

############################################
# Hadi Yapalım Şu İşi
def Doviz():
    # Tanımlamalarımızı Yapalım
    URL = "https://www.doviz.com/"
    Kimlik = {'User-Agent': '@KekikAkademi'} # Websitesine istek yollarken kimlik bilgimizi sunuyoruz

    # WebSitesinin Cevabına bakalım (ilk kontrol)
    #Cevap = requests.get(URL, headers=Kimlik)
    #print(Cevap)

    # Sorun yoksa devam edelim
    Kaynak = requests.get(URL, headers=Kimlik).text # Url'nin içerisindeki bütün html dosyasını indiriyoruz.
    SayfaOku = BeautifulSoup(Kaynak , "html.parser")
    #print(SayfaOku) # bakalım bize gelen veri görüntülenen ile aynı mı?(ikinci kontrol)

    # Siteye girdik. Ne Alıcaz Burdan?
    isim = [] # içerisine veri ekleyeceğimiz boş tablo
    rakam = [] # içerisine veri ekleyeceğimiz boş tablo
    oran = [] # içerisine veri ekleyeceğimiz boş tablo

    # Hadi Kazıyalım!
    for AyristirilanAlan in SayfaOku.findAll('div', attrs={'class':'market-data'}):
        #print(AyristirilanAlan) # ilk ayrıştırmamızı yaptık
        #print(AyristirilanAlan.text) # Bir de kodlardan arındırıp bakalım

        # Parçalamaya devam edelim
        for birinci in AyristirilanAlan.findAll('span', attrs={'class':'name'}):
            #print(birinci) # Bakalım ne geldi
            gelenisim = birinci.text # kodlarından ayıralım
            #print(isim) # kontrol edelim, olmuşsa devam
            isim.append(gelenisim) # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            #Tablo kontrolünü "print(isim)" döngünün dışında yapmayı unutma !

        # şimdi de rakamları çekelim
        for ikinci in AyristirilanAlan.findAll('span', attrs={'class':'value'}):
            #print(ikinci) # Bakalım ne geldi
            gelenrakam = ikinci.text # kodlarından ayıralım
            #print(gelenrakam) # kontrol edelim, olmuşsa devam
            rakam.append(gelenrakam) # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            ## Tablo kontrolünü "print(rakam)" döngünün dışında yapmayı unutma !

        # oranları da çekersek tamamdır
        for ucuncu in AyristirilanAlan.findAll('div', attrs={'class':'change'}):
            #print(ucuncu) # Bakalım ne geldi
            gelenoran = ucuncu.text # kodlarından ayıralım
            #print(gelenoran) # kontrol edelim, boşluklarımız var. boşlukları yok etmeliyiz..
            gelenoran = gelenoran.replace("\n", "") # boşlukları kaldır
            #print(gelenoran) # hala değil
            gelenoran = gelenoran.replace(" ", "") # boşlıkları kaldır :)
            #print(gelenoran) # tamamdır :)
            oran.append(gelenoran) # daha önce oluşturduğumuz boş tabloya verilerimizi ekledik
            ## Tablo kontrolünü "print(oran)" döngünün dışında yapmayı unutma !

    # Tablolarımızı kontrol edelim
    #print(isim)
    #print(rakam)
    #print(oran)
    # haaarika
    for i in range(0,len(isim)): # döngüyü isim tablosunun elemanı kadar sürdür
        print("*"*50 + "\n" + "{} >> {} >> {}".format(isim[i], rakam[i], oran[i]) + "\n" + "*"*50)

    time.sleep(10) # DDoS gibi olmaması için 10 saniye aralık la yap bu işi
    Temizle()
    OturumBilgisi()

# Betiği sonsuz döngüye alıyoruz
while True:
    Doviz()