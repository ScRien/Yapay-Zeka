import random

print("Türkçe Komut Yapay Zekasına Hoşgeldiniz. Sİsteme yönlendiriliyorsunuz.")
def System1():
    kod = input("Çalıştırılacak Kod: ")
    #Print Command
    if kod == "print":
        icerik = input("Metin Giriniz: ")
        sonuc = print("""
        Çalıştırılan Kod: {kods}\n
        İçerik: {iceriks}
        """.format(kods = kod, iceriks = icerik))
    #İnput Command
    if kod == "input":
        soruMetin = input("Sorulacak Metin: ")
        degerİnput = input("{}: ".format(soruMetin))
        sonuc = print("""
        Çalıştırılan Kod: {kods}\n
        Sorulan Metin: {metin}\n
        Verilen Cevap: {cevap}
        """.format(kods = kod, metin = soruMetin, cevap = degerİnput))
    #Değişken Oluşturma Command
    if kod == "degisken":
        degisken = {
            "degiskenAd": input("Değişkenin Adını Giriniz: "),
            "degiskenDeger": input("Değişkenin Değeri: ")
        }
        print(degisken)

while True:
    bilgilendirme = input("""
    Yapay zekanın çalıştırabildiği komutlar:\n
    1 -> print\n
    2 -> input\n
    3 -> değişken oluşturma\n\n
    Not: Eğer yapacağınız işlemden çıkmak istiyorsanız: 'stop' yazınız.
    Bu Seçenekler Hakkında Bilgi Almak istediğiniz rakamı giriniz: """)
    if bilgilendirme == "stop":
        print("İşlemden Çıkıldı..\n\n")
        System1()
    elif bilgilendirme == "1":
        print("""
        Print Komutunun Kullanımı:\n
        Öncelikle Kod Bölümüne; 'print' yazmanız gerek,
        Sonrasında İçerik kısmına; kodun göstereceği metni yazacaksınız.
        """)
    elif bilgilendirme == "2":
        print("""
        İnput Komutunun Kullanımı:\n
        Öncelikle Kod Bölümüne; 'input' yazmanız gerek,
        Sonrasında İçerik kısmına; kodun isteyeceği değeri yazacaksınız.
        """)
    elif bilgilendirme == "3":
        print("""
        Değişken Oluşturma:\n
        Öncelikle Kod Bölümüne; 'degisken' yazmanız gerek,
        Sonrasında icerik kısmına; değişkeninizin adını yazacaksınız.
        """)
    else:
        print("\n\Hata ❗ Hata Numarası: {}\n".format(random.randint(1, 157)))
