🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# KekikRat_v1 Dokümantasyonu
![Python Telegram RAT](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/11-KekikTelegram/images/kapak.jpg "Python Telegram RAT")

`KekikRat_v1` Python diliyle yazılmış, Telegram üzerinden kontrol edilebilen `Uzaktan Erişim amaçlı Truva Atı`dır.

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

### Oluşturduğumuz Bot'a Komutlar Ekleme
Devamı reklamlardan sonra :)

## Python ile Bot'a Bağlanma
Devamı reklamlardan sonra :)

### Oluşturduğumuz Komutlar için Kod Yazma
Devamı reklamlardan sonra :)

________________________________
📃 **Yandex.Disk Bünyemizde 900GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.
