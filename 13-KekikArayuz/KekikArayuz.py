#KekikSiber | t.me/kekiksiber | Python ile Sahte Arayüz Oluşturuyoruz

#######################################################
import tkinter                  # arayüz için
import sys                      # dosya ismi|exit için
from time import sleep          # sleep() için
import platform                 # cihaz bilgileri için
from tkinter import messagebox  # Hata Mesajı için
#######################################################

########################################################
def Muamele():                  # Muamele Fonksiyonumuz
    from tqdm import tqdm
    from random import uniform
    
    liste = ['bağlantı kuruluyor',
        'cpu cevabı.bekleniyor',
        'default klasör aranıyor',
        'bulundu !',
        'patch dosyası oluşturuluyor',
        'patch dosyası doğrulanıyor',
        'doğrulama başarılı',
        'patch indiriliyor',
        'patch indiriliyor',
        'indirme başarılı',
        'doğrulanıyor',
        'patch içeriği okunuyor',
        'yamalanıyor',
        'kuruluyor',
        'yüklemeye hazırlanıyor',
        'internet bağlantısı kontrol ediliyor',
        'kablolar koklanıyor']

    for i in liste:
        label.config(text=i)
        app.update()
        sleep(0.1)

    def Processing():
        pbar = tqdm(list(liste)[::-1])
        for i in pbar:
            pbar.set_description(f'Processing >> {i}')
            label["text"] = f"{i}"
            app.update()
            sleep(0.1)
    Processing()
    
    for i in range(100):
        label["text"] = f"Kuruluyor  %{str(i)}"
        app.update()
        sleep(uniform(0,0.23))
    sleep(2)
########################################################

app = tkinter.Tk()          # tkinter penceremizi açtık
#image = tkinter.PhotoImage(data="""iVBORw0KGgo <BASE64 Kodu(2500+ Satır)> 8coAAAAASUVORK5CYII=""")
    # veya
#image = tkinter.PhotoImage(data=req.urlopen("https://raw.githubusercontent.com/KekikAkademi/KekikPython/master/13-KekikArayuz/lab/lol.png.txt").read())
    # veya
with open("lol.png.txt", "rb") as B64_PNG:
    image = tkinter.PhotoImage(data=B64_PNG.read())

app.iconphoto(1,image)          # Pencere ikonu (Görünmeyecek)
app.title("Lol Money Hack")     # Pencere Başlığı (Görünmeyecek)
app.wm_overrideredirect(True)   # Başlık-Kapat-Küçült Tuşlarının olduğu kısmı kaldırıyoruz
app.attributes("-alpha", 0.9)   # Penceremize hafif şeffaflık katıyoruz

windowWidth = app.winfo_reqwidth()     # penceremizin enlemini aldık
windowHeight = app.winfo_reqheight()   # penceremizin boylamını aldık
positionRight = int(app.winfo_screenwidth()/2.5 - windowWidth/2)  # Pencere konumumuzun enlemini
positionDown = int(app.winfo_screenheight()/2.5 - windowHeight/2) # Pencere konumumuzun boylamını değiştiriyor
app.geometry(f"+{positionRight}+{positionDown}")                  # Pencere konumumuz ayarlıyoruz

#NOT# positionRight ve positionDown 'da pencereyi ortalarken "2.5" rakamında değişiklik yapmanız gerekebilir 

app.resizable(0,0)  # Yeniden boyutlandırmayı kapattık

label = tkinter.Label(image=image,text=" ",compound="top",bg="black",fg="white",cursor="watch") # label'ı ayarladık
label.pack()        # label'imizi görünür yaptık
app.update()        # Tkinter'a tüm ayarları yaptığımızı söyledik.
                    # Böylece sleep verdiğimiz zaman ekrandaki herşeyi gösterip sonra bekleyecek.
                    # Aksi türlü ilk sleep()'i bekliyor ardından uygulamamızı açıyor .
    ## Başladık
sleep(3)            # Arkadaşımızı azıcık bekletelim değil mi :) +knk az bekle yüklenir şimdi

################
label.config(text="Searching LOL Files ..") # 3 saniye bekledikten sonra
                                            # daha önce " " olarak verdiğimiz değere birkaç şeyler yazalım
                                            # Yabancı dil kullanarak "+ adamlar yapmış bee" dedirtebilirsiniz .)
app.update()        # Tekrardan güncelleme vermek zorundayız
sleep(3)            # "Searching LOL Files .." :)
################

################
label["text"] = "Searching LOL Account" # label.config() yapmak yerine label[]'de kullanabilirsiniz .
app.update()        # Tekrardan güncelliyoruz
sleep(2)            # "Searching LOL Account" :)
################

################
Muamele()           # Muamele Fonksiyonumuzu Çağırdık
sleep(2)            # Yine 2 saniye bekletip hatamızı çakalım
    ## Bitirdik

messagebox.showerror("LOL Money Hack","Id1oT.dll not found !") # :) .dll bulunamadı adında bir hata çıkarttık

sys.exit()      # Hata ekranı geçildikten sonra tüm uygulamamızı kapattık

app.mainloop()  # penceremizi aktif ettik 