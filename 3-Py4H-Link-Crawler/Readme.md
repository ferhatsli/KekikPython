🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# Py4H Link Crawler
![Py4H Link Spider-Crawler](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/3-Py4H-Link-Crawler/images/py4h-link-spider-crawler.png)
Hedef web uygulamadaki/sitedeki bağlantı adreslerini (linklerini) toplayan bir araç kodlayacağız.

### **Saldırı Senaryosu:**
Hedef siteye ait kaynak koddaki tüm bağlantı adreslerini listeleyip o linklerde (inject points) Sql Injection, XSS gibi ataklar denenecektir.

### **Algoritma:**
	-   Başla
    -   Hedef siteye git
    -   Kaynak koddaki bağlantıları topla
    -   Bağlantıları düzelt
    -   Ekrana yaz
    -   Bitti

### **Kod Paylaşımı:**
Aşağıdaki kodlarda bilgi fonksiyonu ile kullanıcının aracı nasıl kullanacağı hakkında bilgilendirdik. Gerekli kütüphaneleri aktardık ve tarayıcımızın ayarını yaptık.




### **Notlar:**
    -   Python 3x sürümü ile yazdığımız bu araçta third party modül olarak sadece mechanize kullanılmıştır. Eğer bu modül sisteminizde kurulu değilse kurmanız gerekmektedir. Diğer modüller standart modüller olup sizde kurulu gelmektedir.
    -   Yazdığımız aracın kullanımı python `crawler.py www.hedefsite.com` şeklindedir.

> Bir sonraki yazımızda görüşmek üzere.

[Kaynak](http://python4hackers.com/python-information-gathering-tools/py4h-link-crawler.html "Saygı ve Özlemle...")
________________________________

📃 **Yandex.Disk Bünyemizde 780GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.