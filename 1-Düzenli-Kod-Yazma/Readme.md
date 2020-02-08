# :computer: Python Düzenli Kod Yazma (idiomatic code)
Bildiğiniz gibi `Python` diğer programlama dillerine göre daha kolay bir *syntax*‘a sahip yani; {} vs. çok az kullanıyoruz.
*Python*'da dictionary tanımlarken kullanılıyor fakat bazı programlama dillerinde bir "*hello world!*" yazmak için bile kullanıyorlar.
Bu kadar kolay olması *python*'ı **son zamanlarda aşırı derecesinde geliştirmiştir.**

İnsanlar *python*'u kolay olduğundan dolayı tercih ediyorlar.
Python kolay bir dil fakat; programınızın tam olarak verimli çalışmasını istiyorsanız, bazı kurallara uymanız gerekiyor. **(Uymak zorunda değilsiniz.)**

# Nasıl Düzenli Kod Yazabilirim ?
### Akıllı Yoldan
Size *10 farklı şekilde* `yanlış` ve `doğru` kodlamanın nasıl olduğunu göstereceğim.

## 1. Karşılaştırma Operatörleri
*Karşılaştırma operatörlerini düzenli kullanırsak;* kodumuzun üzerinde pozitif bir artış sağlayacaktır.
Bu yüzden karşılaştırma operatörlerini en iyi nasıl kullanabiliriz, bunu bilmemiz gerekiyor.

**Yanlış** Kullanım;
![Karşılaştırma Operatörleri - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/1-1.png)
Burada `x ve y` - `y ve z` karşılaştırılmış, arasına `and` koyulmuş.
Bu şekilde bir kullanım **gereksiz ve yanlıştır.**
Bu kodu şu şekilde yazabiliriz;

**Doğru** Kullanım;
![Karşılaştırma Operatörleri - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/1-2.png)

## 2. Girintileme
Genel olarak python programcılarında oluşan bir düşüncedir bu; "*az satırlı yazılan kod her zaman daha hızlı çalışır*" **tamamiyle YANLIŞ.**
Bu yüzden şimdi göstereceğim girintilemeyi yapmaktan *kaçının.*

**Yanlış** Kullanım ;
![Girintileme - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/2-1.png)
Burada *2 değişken tanımlamak için* **tek satır kullandık;**
Güzel bir şey yapmış gibi duruyoruz; bir koşullu durum sağlandığında ne yapacağını hemen yanına yazdık.
Burada **kodun tek satır olması onun güzel olduğu anlamına gelmiyor.**
Böyle kullanımdan *kaçının*.

**Doğru** Kullanım;
![Girintileme - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/2-2.png)
Bu şekilde kullanırsanız; **kodunuzun okunurluğu artacaktır.**
Sizin için önemli olan *okunurluk* olduğu için, *doğru olan budur.*

## 3. True-False Kullanımı;
`Doğru` ve `yanlış` durumları; `True` `False` `None` ile karşılaştırmaktır.
**Doğru** olan şeyler her zaman **True**, **Yanlış** durumlar ise **False** olmalıdır.

**Yanlış** Kullanım;
![True-False Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/3-1.png)
`==` operatörüyle böyle bir karşılaştırma yapmak zorunda değiliz.
Doğru kullanımı aşağıdaki şekildedir;

**Doğru** Kullanım;
![True-False Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/3-2.png)
Burada yapmış olduğum `if emre_1` *zaten* `emre_1` **True ise** sağlanacak bir koşul olduğundan; bir daha **==** operatörünü kullanmak sadece kodumuzu uzatacaktır
ve böyle bir kullanımı github‘da göremezsiniz. Doğru kullanım bu şekildedir.

## 4. Ternary Operatör
**Ternary operatör;** *C#, Java, Javascript gibi dillerde* `tek satırlık if – else` yazılımını sağlar.
(Çok koşullu durumlarda kullanılmaz, çünkü kod okunurluğunu azalır.)
Fakat Python böyle bir operatöre sahip değil. :)
Buna benzer bir kullanım yapabiliriz. (Olmaması bize engel değil.)

**Yanlış** Kullanım;
![Ternary Operatör - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/4-1.png)
İşte **o kadar koşullu durum olmadığı zaman kullanılır** demiştim.
Burada çok koşullu bir durum yok, biz de ternary operatörlerine benzer bir şekilde kullanacağız.

**Doğru** Kullanım;
![Ternary Operatör - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/4-2.png)
Görmüş olduğunuz gibi hem **satır sayısı azaldı** hem de **daha okunur oldu.**
Burada eğer **emre True ise 1 e eşit** olacak **değilse 0 a eşit** olacaktır.

## 5. "in" Kelimesi Kullanılması
*Bir değişkenin gereksiz yere diğer değerlerle sürekli tekrar edilmesi* **yanlış bir durumdur.** Örnek verecek olursak;

**Yanlış** Kullanım;
!["in" Kelimesi - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/5-1.png)
Bu şekilde `==` operatörüyle **kodu uzatmak gereksizdir.**
Yerine şöyle bir şey kullanacağız;

**Doğru** Kullanım;
!["in" Kelimesi - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/5-2.png)
Görmüş olduğunuz gibi; *bir liste içerisine karşılaştırılacak değeri girdim* ve **benim ismimin o liste içerisinde olup olmamasına göre karşılaştırma yaptım.** :)
*Bu şekilde kullanım,* **kodu kısaltır ve daha doğrudur.**

## 6. Fonksiyon içerisinde karşılaştırma ve Return
**Yanlış** Kullanım;
![Fonksiyon içerisinde karşılaştırma ve Return - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/6-1.png)
Zaten `==` operatörü *eğer eşitse* **True** *değilse* **False** döndürüyor.
Böyle yapmamıza gerek yok.
Şu şekilde yapmalıyız;

**Doğru** Kullanım;
![Fonksiyon içerisinde karşılaştırma ve Return - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/6-2.png)
Burada; *eğer x y‘e eşitse* **True** *değilse* **False** döndürecek. :)

## 7. Çoklu Atama
**Eğer** *3 veya 5 değere* **aynı değeri atayacaksanız;**
**tek satırda atamanız daha doğru olur.**

**Yanlış** Kullanım;
![Çoklu Atama - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/7-1.png)
*Böyle yapmak zorunda değilsiniz.*
**Kodunuzun okunurluğu daha güzel olsun!**
Şöyle yapmak daha doğrudur.

**Doğru** Kullanım;
![Çoklu Atama - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/7-2.png)
Bu özelliği *çoklu atama yapacağınızda;* **yani atayacağınız değişkenler, aynı değeri tutacağı zaman** kullanmalısınız.

## 8. Stringleri Biçimlendirme
Yine çok yapılan bir yanlış; **stringleri biçimlendirirken** `+` operatörünün kullanılmasıdır.
Bunun yerine; **python3 ile gelmiş olan** `format` fonksiyonunu kullanacağız.  

**Yanlış** Kullanım;
![Stringleri Biçimlendirme - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/8-1.png)

**Doğru** Kullanım;
![Stringleri Biçimlendirme - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/8-2.png)

Arkadaşlar `+` operatörüyle yapmak **yanlış değildir.**
Ancak bu olay şuna benziyor; günümüzde akıllı telefon varken tuşlu telefon kullanmak gibi.. Eski teknoloji kullanmak yani..

## 9. List Comprehension Kullanım
Eğer bir liste oluşturacaksak; `list comprehension`larını kullanmak çok daha güzel olacaktır.
Şimdi doğru ve yanlış(kötü) kullanımlarını verelim;

**Yanlış** Kullanım;
![List Comprehension Kullanım - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/9-1.png)

Burada belki `if not` kısmını anlamamış olabilirsiniz;
oradaki `if not` kısmı şu şekildedir;
şimdi **sayının 2 den bölümüne bakılacak,**
*eğer 2 den bölümü* **0 ise;**
yani 0 ın `bool` değeri **False olduğu için** `if not` diyoruz.
False oluyor; o zaman da 2 ye bölünenleri veriyor bize.
**not demeyip if deseydik** *o zaman true döndürenleri verirdi.*
Tabii bu şekilde kullanmak uzun yoldur daha kısa yolu var bu şekilde doğrusu.

**Doğru** Kullanım;
![List Comprehension Kullanım - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/9-2.png)

Görmüş olduğunuz gibi; **kodu ne kadar kısalttık.**
Eğer bir listeye verilerimizi saklayacaksak; bu şekilde yapmak en doğrusudur.
Github'da da böyle görürsünüz.

## 10. Set Comprehension
Aslında listenin sözlüğün kümenin hepsinde `comprehension` kullanmak doğrudur.
İşte bu yüzden kullanmalıyız. :)

**Yanlış** Kullanım;
![Set Comprehension - Yanlış Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/10-1.png)

**Doğru** Kullanım;
![Set Comprehension - Doğru Kullanım](https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/1-D%C3%BCzenli-Kod-Yazma/images/10-2.png)


**Eğer Open-Source developersanız;** `kodunuzun okunulurluğunu arttırmak için` *böyle yöntemleri kullanmalısınız.*

Yanlış değil, kullanabilirsiniz ama böyle bir kullanım görmezsiniz. :)

#
> Bu readme sayfası oluşturulurken [prose.io](http://prose.io/ "prose.io") ve [stackedit.io](https://stackedit.io/app "stackedit.io") araçlarından yardım alınmıştır..
> Emojiler için [webfx](https://www.webfx.com/tools/emoji-cheat-sheet/ "Emoji Cheat Sheet") sayfası kullanılmıştır.
