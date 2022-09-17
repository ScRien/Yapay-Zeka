import random

print("Merhaba, bu bir yapay zekadır. Lütfen değerleri doğru girerek yapay zekanın algılamasını sağlayınız.")
dilTercih = int(input("Dil Seçiniz:\n1 -> Türkçe\n2 -> İngilizce\n3 -> Çince\n4 -> Rusça\nSeçiminiz: "))
# Türkçe
if dilTercih == 1:
    def turkceSystem():
        print("Türkçe Komut Yapay Zekasına Hoşgeldiniz. Sİsteme yönlendiriliyorsunuz.")
        onof = ["online", "ofline"]
        onofsecim = random.choice(onof)

        if onofsecim == "online":
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
                

        if onofsecim == "offline":
            print("Yapay zeka'ya bağlanılamadı.")

    
    bilgilendirme = input("""
    Yapay zekanın çalıştırabildiği komutlar:\n
    1 -> print\n
    2 -> input\n
    3 -> değişken oluşturma\n\n
    Not: Eğer yapacağınız işlemden çıkmak istiyorsanız: 'stop' yazınız.
    Bu Seçenekler Hakkında Bilgi Almak istediğiniz rakamı giriniz: """)
    if bilgilendirme == "stop":
        print("İşlemden Çıkıldı..\n\n")
        turkceSystem()
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


# İngilizce


if dilTercih == 2:
    def englishSystem():
        print("Welcome to Turkish Command Artificial Intelligence. You are being redirected to the system.")
        onof = ["online", "ofline"]
        onofsecim = random.choice(onof)

        if onofsecim == "online":
            kod = input("Code to Run: ")
            #Print Command
            if kod == "print":
                icerik = input("Enter Text: ")
                sonuc = print("""
                Code: {kods}\n
                Content: {iceriks}
                """.format(kods = kod, iceriks = icerik))
            #İnput Command
            if kod == "input":
                soruMetin = input("Text to Ask: ")
                degerİnput = input("{}: ".format(soruMetin))
                sonuc = print("""
                Code: {kods}\n
                Asked Text: {metin}\n
                Answer Given: {cevap}
                """.format(kods = kod, metin = soruMetin, cevap = degerİnput))
            #Değişken Oluşturma Command
            if kod == "variable":
                degisken = {
                    "variableName": input("Enter the Name of the Variable: "),
                    "variableValue": input("Value of Variable: ")
                }
                print(degisken)
                

        if onofsecim == "offline":
            print("Failed to connect to AI.")

    
    bilgilendirme = input("""
    Commands that AI can run:\n
     1 -> print\n
     2 -> input\n
     3 -> variable creation\n\n
     Note: If you want to exit the operation you are about to do, type 'stop'.
     Enter the number you want to get information about these options: """)
    if bilgilendirme == "stop":
        print("Process Exited..\n\n")
        englishSystem()
    elif bilgilendirme == "1":
        print("""
    Usage of Print Command:\n
         First of all, to the Code Section; you need to type 'print',
         Then to the Content section; you will write the text that the code will display.
        """)
    elif bilgilendirme == "2":
        print("""
    Usage of Input Command:\n
         First of all, to the Code Section; you need to type 'input',
         Then to the Content section; You will write the value that the code will ask for.
        """)
    elif bilgilendirme == "3":
        print("""
    Creating Variables:\n
         First of all, to the Code Section; you have to write 'variable',
         Then to the content part; you will write the name of your variable.
        """)
    else:
        print("\n\nError ❗ Error Number: {}\n".format(random.randint(1, 157)))

# Çince
if dilTercih == 3:
    def englishSystem():
        print("欢迎来到土耳其指挥人工智能。 您正在被重定向到系统。")
        onof = ["online", "ofline"]
        onofsecim = random.choice(onof)

        if onofsecim == "online":
            kod = input("要运行的代码: ")
            #Print Command
            if kod == "打印":
                icerik = input("输入文字: ")
                sonuc = print("""
                代码: {kods}\n
                内容: {iceriks}
                """.format(kods = kod, iceriks = icerik))
            #İnput Command
            if kod == "输入":
                soruMetin = input("要问的文字: ")
                degerİnput = input("{}: ".format(soruMetin))
                sonuc = print("""
                代码: {kods}\n
                询问文字: {metin}\n
                给出的答案: {cevap}
                """.format(kods = kod, metin = soruMetin, cevap = degerİnput))
            #Değişken Oluşturma Command
            if kod == "多变的":
                degisken = {
                    "变量名": input("输入变量的名称: "),
                    "变量值": input("变量值: ")
                }
                print(degisken)
                

        if onofsecim == "offline":
            print("Failed to connect to AI.")

    
    bilgilendirme = input("""
    AI 可以运行的命令：\n
      1 -> 打印\n
      2 -> 输入\n
      3 -> 变量创建\n\n
      注意：如果要退出即将执行的操作，请键入“停止”。
      输入您要获取有关这些选项的信息的号码： """)
    if bilgilendirme == "停止":
        print("进程退出..\n\n")
        englishSystem()
    elif bilgilendirme == "1":
        print("""
    打印命令的用法:\n
          首先，到代码部分； 您需要输入“打印”，
          然后到内容部分； 您将编写代码将显示的文本。
        """)
    elif bilgilendirme == "2":
        print("""
    输入命令的用法:\n
          首先，到代码部分； 您需要输入“输入”，
          然后到内容部分； 您将编写代码要求的值。
        """)
    elif bilgilendirme == "3":
        print("""
    创建变量:\n
          首先，到代码部分； 你必须写'变量'，
          然后到内容部分； 您将编写变量的名称。
        """)
    else:
        print("\n\错误 ❗ 错误 数字: {}\n".format(random.randint(1, 157)))



# Rusça


if dilTercih == 4:
    def englishSystem():
        print("Добро пожаловать в Турецкий командный искусственный интеллект. Вы перенаправлены в систему.")
        onof = ["online", "ofline"]
        onofsecim = random.choice(onof)

        if onofsecim == "online":
            kod = input("код для запуска: ")
            #Print Command
            if kod == "Распечатать":
                icerik = input("Введите текст: ")
                sonuc = print("""
                Код: {kods}\n
                Содержание: {iceriks}
                """.format(kods = kod, iceriks = icerik))
            #İnput Command
            if kod == "вход":
                soruMetin = input("Текст, чтобы спросить: ")
                degerİnput = input("{}: ".format(soruMetin))
                sonuc = print("""
                Код: {kods}\n
                Запрашиваемый текст: {metin}\n
                Ответ дан: {cevap}
                """.format(kods = kod, metin = soruMetin, cevap = degerİnput))
            #Değişken Oluşturma Command
            if kod == "переменная":
                degisken = {
                    "имя_переменной": input("Введите имя переменной: "),
                    "значение переменной": input("Значение переменной: ")
                }
                print(degisken)
                

        if onofsecim == "offline":
            print("Не удалось подключиться к ИИ.")

    
    bilgilendirme = input("""
    Команды, которые может выполнять ИИ:\n
      1 -> печать\n
      2 -> ввод\n
      3 -> создание переменных\n\n
      Примечание. Если вы хотите выйти из операции, которую собираетесь выполнить, введите «стоп».
      Введите номер, который вы хотите получить информацию об этих опциях: """)
    if bilgilendirme == "остановка":
        print("Процесс завершен..\n\n")
        englishSystem()
    elif bilgilendirme == "1":
        print("""
    Использование команды печати:\n
          Прежде всего, в раздел Кодекса; вам нужно ввести «печать»,
          Затем в раздел «Контент»; вы напишете текст, который будет отображать код.
        """)
    elif bilgilendirme == "2":
        print("""
    Использование команды ввода:\n
          Прежде всего, в раздел Кодекса; вам нужно ввести «ввод»,
          Затем в раздел «Контент»; Вы напишете значение, которое запросит код.
        """)
    elif bilgilendirme == "3":
        print("""
    Создание переменных:\n
          Прежде всего, в раздел Кодекса; вы должны написать «переменная»,
          Затем к содержательной части; вы напишите имя вашей переменной.
        """)
    else:
        print("\n\ошибка ❗ номер ошибки: {}\n".format(random.randint(1, 157)))