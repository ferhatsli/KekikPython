🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# Telegram Botu Oluşturma ve Kazıyıcıya Entegrasyon
![Python Telegram Entegrasyon](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/11-KekikTelegram/images/kapak.jpg)

Daha önce yazmış olduğumuz [**KekikDoviz**](https://github.com/KekikAkademi/KekikPython/tree/master/8-KekikDoviz) `Kazıyıcı`*(Scraper)* betiğimizin elde ettiği verileri Telegram Botuna entegrasyonunu konu alacağız.

## Telegram Botu Oluşturma
Telegramda bot oluştururken babaların babası [BotFather](https://t.me/BotFather)'dan yardım alıyoruz.

- İlk önce *BotFather*'a **yeni bir bot oluşturma isteği** yolluyoruz;
>`/newbot`
- Daha sonra botumuza **isim** veriyoruz;
>`@KekikAkademi Python Veri Kazıma Örneği`
- Ardından botumuz için **kullanıcı adı** oluşturuyoruz. Bu kullanıcı adı `_bot` veya `bot` **ile bitmek zorunda.**
>`KekikAkademiPythonBot`
- Bize döndürdüğü token'i bir yere kayıt ediyoruz. (Token'e daha sonra da ulaşılabiliyor, yeni token istenebiliyor. Çok dert bir durum değil.)
>`1052180975:AAHnsgm1U3pygiaY1tWxVUpnoeh-byvECLg`
>Bu token artık geçersiz olduğu için gönül rahatlığıyla paylaşabiliyorum :)

![Telegram Bot Oluşturma](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/11-KekikTelegram/images/Telegram-Bot-Olusturma.png)

> **`/mybots` komutu ile oluşturduğumuz bota açıklama fotoğraf vs. ekleyip değiştirebilir; tokeni yenileme işlemlerini yapabiliriz..**

- Oluşturduğumuz bot'a girip (*[@KekikAkademiPythonBot](https://t.me/KekikAkademiPythonBot)*)  `/start` diyerek **botu başlatıyoruz.**

### Bot Kontrolü ve Chat id Öğrenmek
- Botumuzun düzgün çalışıyor olduğunu teyit etmek için `https://api.telegram.org/bot{token}/getMe` adresini kontrol ediyoruz.

>`https://api.telegram.org/bot1052180975:AAHnsgm1U3pygiaY1tWxVUpnoeh-byvECLg/getMe`

![getMe Bağlantısı](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/11-KekikTelegram/images/getMe.png)

- Ardından bota (*[@KekikAkademiPythonBot](https://t.me/KekikAkademiPythonBot)*) *herhangi bir mesaj yazarak* **botla etkileşime geçiyoruz.**

- Daha sonra `https://api.telegram.org/bot{0}/getUpdates` adresini kullanarak **gelen verilerin json çıktısı**nı elde ediyoruz.  Bu çıktıda **bizim için önemli olan `id` parametresidir.** Bu parametrenin değerini de not alalım.

![getUpdates](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/11-KekikTelegram/images/getUpdates.png)

**Şu an elimizde `token` ve `id` parametreleri var.** 
> Artık bu iki parametre ile botumuzu kontrol edeceğiz..

## Betiği Telegram Botuna Bağlama
Betiğin döndürdüğü veriyi Telegram Botumuza iletmek için **Telegram'ın bize sunduğu URL yapısını kullanacağız.**
*Bu URL yapısı;*
`https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}`
> Telegram sendMessage URL Yapıları Hakkında Dökümantasyon --> https://core.telegram.org/bots

Daha önce yazmış olduğumuz [**KekikDoviz**](https://github.com/KekikAkademi/KekikPython/tree/master/8-KekikDoviz) `Kazıyıcı`*(Scraper)* betiğimizde;
Elde ettiğimiz verileri `for` döngüsü içinde çevirip `print` ile ekrana yazdırmıştık.
Aynı `for` döngüsü içine entegrasyonumuzu sağlarsak; **ekrana yazdırmasıyla eş zamanlı olarak telegram botumuza iletecektir..** 

	########################
	###Telegram Entegrasyonu
	gonderilecekYazi = "{} >> {} >> {}".format(isim[i], rakam[i], oran[i]) # Gönderilecek Yazı tanımlamamızı yaptık
	
	token = "1052180975:AAHnsgm1U3pygiaY1tWxVUpnoeh-byvECLg"  # Telegram Tokenimizi tanımladık
	chat_id = "717569643"  # Telegram Chat id mizi tanımladık

	requests.post(url='https://api.telegram.org/bot{0}/sendMessage'.format(token), data={'chat_id': chat_id, 'text': gonderilecekYazi}).json()

	###Telegram sendMessage URL Yapıları Hakkında Dökümantasyon --> https://core.telegram.org/bots
	############################

![@KekikAkademi Python Veri Kazıyıcı Telegram Entegrasyonu](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/11-KekikTelegram/images/Sonu%C3%A7.png)

#### _Kodların Tamamına_ [**Burdan**](https://github.com/KekikAkademi/KekikPython/blob/master/11-KekikTelegram/KekikTelegram.py "KekikTelegram.py") _Ulaşabilirsiniz.._

[Kaynak 1](https://steemit.com/utopian-io/@overmedia/let-s-make-telegram-bot-with-python-tuerkce) - [Kaynak 2](http://unalfaruk.com/2017/01/21/python-ile-telegram-bot/) - [Kaynak 3](https://medium.com/@mcakir/ki%C5%9Fisel-bildirimleriniz-i%C3%A7in-telegram-botu-olu%C5%9Fturmak-6eb10d51383b)

________________________________
📃 **Yandex.Disk Bünyemizde 900GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.
