🕊 Bu döküman [**@KekikAkademi**](https://t.me/KekikAkademi "Telegram: @KekikAkademi") için oluşturulmuştur. ✌🏼
________________________________
# Python ile Veri Kazıma
![Veri Kazımanın Çalışma Şeması](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/8-KekikDoviz/images/1-Veri-Kazimanin-Calisma-Semasi.jpeg)
Veri Kazıma iki Aşamadan Oluşur;
 1. **Web Crawling**
 2. **Web Scraping**

## Veri Kazıma Nedir?
Veri kazıma diğer bir adıyla Data Scraping, Web sitelerinden veri çıkarma işlemidir.

### Neden Veri Kazırız?
Web üzerinde birçok veri bulunuyor. Veri kazıma’da bu **veri toplama işlemini otomatikleştirir.** *Dağıtık halde olan verileri daha düzgün şekilde sunar.*
İnternet’ten kazınan verilerle birçok çalışma yapılabilir. Bunların en yaygınlarından biri fiyat karşılaştırmasıdır.

## Web Crawling Nedir?
**Web Crawling**, *HTTP bağlantısı ile herhangi bir site üzerinde gezinmek ve hedef site üzerinde yeralan linkleri toplamaktır.*
Bu linkler tüm site olabileceği gibi sınırlı sayıda da olabilir.
İşte bu link toplama işlemini yerine getiren yapıya da _Web Crawler_ denilmektedir.
`Web Crawler`, `Web Spider`, `Robot` veya `Bot` hangi isimle hitap ederseniz; hepsi aynı anlama gelmektedir ve yaptıkları iş de aynıdır.

### Çalışma Mantığı
Web Crawler’ların çalışma mantığı karmaşıktır ama iyi bir analiz ve sistemli çalışma ile ortaya güzel bir sonuç çıkarılabilir.

Öncelikli olarak; veri almak istediğiniz site veya platformu belirlemeniz gerekir.
Belirleme işleminden sonra hedefteki bu adresin iyi analiz edilmesi gerekir. Analizden kastım; verilerin bulunduğu sayfalardır.
Bu sayfaların kurulma ve dolaşım şeması detaylı olarak incelenmelidir. Örneğin; bazı platformlar size istediğiniz verileri hemen göstermezler. Bir butona veya text’e tıklamanızı veyahut bir şeyleri sürükleyip bırakmanızı isteyebilirler.
Bunların hepsi birer handikaptır ve çözülmesi gereken birer sorundur.

_Web Crawler_’ın temelde yapacağı şey şudur; **belirlenen adresin tüm linklerini taramak ve listelemektir.** *Daha sonra da listelediği bu linklere sırasıyla gider.*
Bu işlemi otomatize etmek de `Web Crawler` kavramını doğurur.

## Web Scraping Nedir?
*Web Crawler*, betirlenen hedef adresteki link’leri tarar ve bu linleri bir liste şeklinde tutar. Yani bir link kuyruğu oluşturur. Bu oluşturulan kuyruktaki link’lere sırasıyla uğrar ve yeni link’ler varsa onları da listesine ekler – tabiki listede olmayan linkleri-.
*Web crawler bir link’e uğradığı zaman* **devreye Web Scraping kavramı girer.**
`Web Scraping`, link’teki belirtilen alanların toplanması işlemidir. Yani bir nevi; veri toplama veya yığından veri çıkarma olayıdır.
`Web Crawler` ve `Web Scraping` *birbirleriyle partner olan kavramlar.* Yani birbirlerini *tamamlayıcı kavramlar* desek herhalde yanlışlık olmaz.

Şimdi örnek bir senaryo oluşturalım;
Elimizde örnek bir x web sitesi olduğunu varsayalım. Bu x web sitesinde bulunan ve reel kişilere ait olan; [Ad, Soyad, Telefon, Şehir] alanlarını almak istiyoruz.
Yapacağımız işlem şöyle olacaktır;
Belirlenen adresteki linkler gezilecek (crawling),
Sonrasında da gezilen sayfalardaki veriler toplanacaktır (scraping).
Yani; istediğimiz alanları sayfadan koparıp almamız gerekir..
Burdan sonrası da verilen düzenli bir şekilde saklanması işlemidir.

## Veri Kazıma Stratejisi
Veri kazıma stratejisinin çok önemli olduğunu düşünüyorum, bir sitedeki bütün veriyi otomatik şekilde kazımak istiyorsak bir plana ihtiyacımız vardır.
Burada kısaca veriyi hangi yollarla nasıl bir Pipeline’da kazıyacağımızı belirlemeliyiz.
![Veri Kazıma Stratejisi](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/8-KekikDoviz/images/2-Veri-Kazima-Stratejisi.png)

## Nelere Dikkat edilmelidir?
Web Scraping yaparken dikkat edilmesi gereken en önemli hususlar; doğru bilgiyi almak ve bilgi bozulmasının önüne geçmek.

Doğru bilgiyi almaktan kastım; işaretlenen alandaki veri alındıktan sonra bu verinin temizlenmesi işlemidir. Bilgi genelde temiz gelir lakin bazen bazı durumlarla karşılaşabilirsiniz. Örneğin; bilgi içerisinde bir takım özel işaretlemeler veya diğer başka element’ler, JavaScript kodları vs olabilir. Bu da demektir ki doğru bilgiye henüz ulaşamamışsınız. Böyle bir durumda alınan veriler, temiz olsalar bile temizleme yani sanitize işlemine tabi tutulmaları gerekir. Bu işlemi; web adresleri, mail adresleri veya telefon numaraları için de kullanabilirsiniz, hatta kullanmalısınız da. Çünkü; web adresi yerine örneğin; www yazıp bırakmış olabilirler. Dolayısıyla doğru bilgiye ulaşmak için; veriler temizlenmeli ve kalan değer varsa alınmalıdır. Aksi halde kalan değer yoksa; zaten kimsenin işine yaramaz..!

Bilgi bozulmasının önüne geçmekten kastım ise; her sayfanın karakter kodlaması UTF-8 değildir. Farklı karakter kodlaması kullanılmış olabilir. Dolayısıyla siz bu değerlere ulaştığınız da muhtemelen bilgi bozulmasıyla karşı karşıya kalabilirsiniz. Bunun da önüne geçmek için; web sayfası scraping edilirken sayfanın karakter kodlamasını UTF-8 olarak veya ISO-8859- 1 olarak değiştirmenizdir. Aksi halde; aldığınız değerler bozulmuş yapıda olacaktır. Bu bozulmuş değerleri daha sonra da düzenleyebilirsiniz fakat bu oldukça zor ve meşakkatli bir durum teşkil edecektir. O yüzden hiç bu işe girmeden; scraping sırasında bilgi bozulmasının önüne geçmeliyiz.

## Verilerin Saklanması
Crawling işleminden sonra; Scraping işlemini de yaptığımızı varsayalım. Veriler elimize öbek öbek geliyor. Bu verilerin saklanması sorunsalı karşımıza çıkacaktır. Bu verilerin saklanması için; .json veya .txt dosyalarından medet ummayalım. Böyle bir düşünceniz varsa hemen aklınızdan çıkarın..! Çünkü sistemin yavaşlamasına ve bir süre sonra yanıt verememesine neden olacaktır. Bunun yerine; MySQL tercih edilebilir bir seçenek lakin SQLite tercih edilemez. SQLite hem veri saklama kapasitesi bakımından hem de MySQL seviyesinde bir pratikliğe sahip olamaması bakımından tercih dışıdır. Bana sorarsanız; MySQL’den de ziyade eşzamanlı bir veri tabanı kullanmanızı size tavsiye ederim. Örneğin; Firebase gibi. Firebase yerine; NoSQL tabanlı bir veri tabanı da tercih edebilirsiniz. MySQL kullanmayın demiyorum, elbette MySQL tercih edilebilir bir seçenektir diyorum.

Verilerin düzgün tasnif edilmesi, ilerleyen zamanlarda kullanım açısından oldukça önemlidir. O yüzden alınan veriler; temiz ve ham veri olmalıdır. Yani istenildiği zaman üzerinde işlem yapılmadan kullanılabilinmelidir.

[Kaynak - 1](https://www.emrecanoztas.com/)
[Kaynak - 2](https://medium.com/kaveai)
________________________________
📃 **Yandex.Disk Bünyemizde 900GB veri olmuştur.**

_Paylaşılan Kursların Tümünü_ [**@KekikKahve**](https://t.me/KekikKahve) _Grubu notlarından Çağırabilirsiniz.._

🕊️ Bize **oy verip** _paylaşarak_ destek olmaya ne dersin? ✌🏼
#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.