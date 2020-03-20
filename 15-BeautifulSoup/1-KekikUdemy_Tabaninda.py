#!/usr/bin/env python
#! -*- coding: utf-8 -*-
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#####################################################################################
import requests                 # Websitelerine istek atmamızı sağlayacak arkadaş   #
from bs4 import BeautifulSoup   # HTML veya XML dosyalarını okuyan arkadaş          #
import re                       # Ayrıştırıcı Arkadaş                               #
import os                       # Dizinler ve dosyalarla çalışmak için              #
from time import sleep          # sleep() için                                      #
#####################################################################################

#-------------------------------------------------------------------------------------------#
udemy_baslik = []                                                   # Boş Tablo Oluşturduk  #
udemy_link = []                                                     # Boş Tablo Oluşturduk  #
#-------------------------------------------------------------------------------------------#

for sayfa in range(1, 3):                                           # Sayfa Sayısı | örn:(1, 3) {2 Sayfa Tarar [1-2]}
    os.system("cls")                                                # Terminal'i Temizle
    
    #----------------------------------------------------------------------------------------------------------------------------------#
    sayfa = str(sayfa)                                              # int olan değerimizi str yapıyoruz
    link = 'https://www.discudemy.com/language/Turkish/' + sayfa    # sayfalar arasında gezinmek için
    kimlik = {'User-Agent': '@KekikAkademi'}                        # Websitesine istek yollarken kimlik bilgimizi sunuyoruz
    istek = requests.get(link)                                      # link'e istek göderiyoruz ve gelen veriyi kaydediyoruz
    kaynak = BeautifulSoup(istek.text, 'html5lib')                  # bitifulsup ile html'i işlememiz gerekiyor / html5lib'i kullandık
    print(f"\tSayfa : {link}")                                      # Bulunduğun Link'i Terminale Yazdır
    print("\t\t Değişken : // link\n")                              # ilgili Değişkeni Terminale Yazdır
    #sleep(1)                                                        # Bekleme Ver
    #----------------------------------------------------------------------------------------------------------------------------------#

    #---------------------------------------------------------------------------------------------------------------------#
    for heading in kaynak.findAll('a', {'class': 'card-header'}):   # kaynak'tan | <a class'ı = card-header olanları tut
        heading = heading.text                                      # Yazı Formatına Çevir
        udemy_baslik.append(heading)                                # Tablomuza Yerleştir
    print(f"\tBaşlık Yakaladım : {udemy_baslik}")                   # Bulunduğun Başlık'ı Terminale Yazdır
    print("\t\t Değişken : // udemy_baslik\n")                      # ilgili Değişkeni Terminale Yazdır
    #sleep(1)                                                        # Bekleme Ver
    #---------------------------------------------------------------------------------------------------------------------#

    #-----------------------------------------------------------------------------------------------------------------------#
    for discudemy_linkler in kaynak.findAll('a', attrs={                        # kaynak'tan | <a olanları _ ve
        'href': re.compile("^https://www.discudemy.com/Turkish/")}):            # href="../Turkish/' olan linkleri tut
        gelen_discudemy = discudemy_linkler['href']                             # dönen verideki linkleri tut
        discudemy_go_html = requests.get(gelen_discudemy)                       # onlara istek gönder
        discudemy_go_kaynak = BeautifulSoup(discudemy_go_html.text, 'html5lib') # kaynağını al
        print(f"Burdayım : {gelen_discudemy}")                                  # Bulunduğun Link'i Terminale Yazdır
        print("\t Değişken : // gelen_discudemy\n")                             # ilgili Değişkeni Terminale Yazdır
        #sleep(1)                                                                # Bekleme Ver
        
        #-------------------------------------------------------------------------------------------------------------------#
        for discudemy_go_linkler in discudemy_go_kaynak.findAll('a', attrs={    # aldığın kaynaktan | <a olanları _ ve
            'href': re.compile("^https://www.discudemy.com/go/")}):             # href="../go/kurs-adi" olan linkleri tut
            gelen_discudemy_go = discudemy_go_linkler['href']                   # dönen verideki linkleri tut
            udemy_html = requests.get(gelen_discudemy_go)                       # onlara istek gönder
            udemy_kaynak = BeautifulSoup(udemy_html.text, 'html5lib')           # kaynağını al
            print(f"Burdayım : {gelen_discudemy_go}")                           # Bulunduğun Link'i Terminale Yazdır
            print("\t Değişken : // gelen_discudemy_go\n")                      # ilgili Değişkeni Terminale Yazdır
            #sleep(1)                                                            # Bekleme Ver
            
            #---------------------------------------------------------------------------------------------------------------#
            for udemy_linkler in udemy_kaynak.findAll('a', attrs={              # aldığın kaynaktan | <a olanları _ ve
                'href': re.compile("^https://www.udemy.com/")}):                # href="../www.udemy.com/" olan linkleri tut
                gelen_udemy = udemy_linkler['href']                             # dönen verideki linkleri tut
                udemy_link.append(gelen_udemy)                                  # Tablomuza Yerleştir
                print(f"Burdayım : {gelen_udemy}")                              # Bulunduğun Link'i Terminale Yazdır
                print("\t Değişken : // gelen_udemy\n")                         # ilgili Değişkeni Terminale Yazdır
                #sleep(1)                                                        # Bekleme Ver
    
    os.system("cls")                                                # Terminal'i Temizle
    #-----------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------#
print("\n\n\n\tSiliyorum...")               # Sildiğini Bildir
sleep(2)                                    # 2sn Bekle
os.system("cls")                            # Terminal'i Temizle
print("\n\n\n\tKursları Listeliyorum...")   # Listelediğini Bildir
sleep(2)                                    # 2sn Bekle
os.system("cls")                            # Terminal'i Temizle
#-------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------------#
for adet in range(0, len(udemy_baslik)):                    # 0'dan Başlayarak, Dönen "başlık" sayısı kadar "adet" oluştur
    gelen_udemy_kaydet = open("DiscUdemy.txt", "a+")        # .txt oluştur
    gelen_udemy_kaydet.write(f"{udemy_baslik[adet]}\n")     # Başlık[adet] yaz satır atla
    gelen_udemy_kaydet.write(f"{udemy_link[adet]}\n\n")     # Link[adet] Yaz satır atla, satır atla
    gelen_udemy_kaydet.close()                              # dosyayı kapat
#-------------------------------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------#
icerik = open("DiscUdemy.txt", "r").read()                  # Dosyayı oku   #
print(icerik)                                               # Ekrana Yaz    #
os.remove("DiscUdemy.txt")                                  # Dosyayı Sil   #
#---------------------------------------------------------------------------#