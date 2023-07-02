###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

# Veri Yapıları
# Sayısal(int,float,complex)
# karakter dizileri
# boolen
# tuple
# set

x = 8
type(x)

y = 3.2
type(y)


z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)


l = [1, 2, 3, 4,"String",3.2, False]
type(l)

# Kapsayıcıdır
# Sıralıdır. index'ler üzerine işlemler yapabiliyoruz.
# Değiştirilebilir


d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

# Sırasızdır.
# Kapsayıcıdır.
# Değiştirilebilir
# key değeri unique


t = ("Machine Learning", "Data Science")
type(t)
t[0]
# Değiştirilemez
# Kapsayıcı
# Sıralıdır


s = {"Python", "Machine Learning", "Data Science","Python"}
type(s)


# Değiştirilebilir
# Sırasız + eşsiz
# Kapsayıcı


###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."
text.upper()
text.upper().replace(","," ").replace("."," ").split()

# Bonus Soru: Tüm harfleri kucuk harfe cevirmek istersek?
text.lower()

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)
# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Bonus Soru: Sıfırıncı ve onuncu indexi tek listede görmek istersek?
[lst[0], lst[10]]
[lst[0] + lst[10]]


# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
lst

# Adım 5: Yeni bir eleman ekleyin.
lst.append("miuul")
lst

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
# Hangi indexe alacagım?
# Hangi nesneyi alacagım?
lst.insert(8,"N")
lst


# Bonus: Bir listeye baska bir liste eklemek istersek:
# create a list
prime_numbers = [2, 3, 5]
# create another list
numbers = [1, 4]
# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)
numbers

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

# dict = {key:value}

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.
dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Guncellemek?

dict.update({"Daisy": ["England",13]})
dict

# Baska bir yöntem:
dict["Daisy"] = ["England",15]
dict

dict["Daisy"][1] = 20
dict


# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
#yeni bir deger eklemek:

dict.update({"AHMET": ["TURKEY",24]})
dict

dict["Dilara"] = ["İstanbul",24]
dict



# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")
dict

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################
#Fonksiyon:

l = [2,13,18,93,22]

cift=[]
tek=[]
def sayı(liste):
    for i in liste:
        if i % 2 ==0:
            cift.append(i)
        else:
            tek.append(i)
    return cift,tek

 cift,tek = sayı(l)

#Bonus: List Comp

cift_sayı = [i for i in l if i % 2 == 0]
tek_sayı = [i for i in l if i % 2 != 0]

#----------------------------------------

cift_sayilar=[]
tek_sayilar=[]
[cift_sayilar.append(i) if i % 2 == 0  else tek_sayilar.append(i) for i in l  ]

#ikisini bir listede ayrı listeler halinde görmek istersek:
tum_sayılar =[[],[]]
[tum_sayılar[0].append(i) if i % 2 == 0  else tum_sayılar[1].append(i) for i in l  ]



###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

# enumarate index bilgilerini de tutar.
# indexin önemli oldugu noktalarda kullanmak faydalı olur.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,name in enumerate(ogrenciler):
    if i < 3:
        i+=1
        print("Mühendislik Fakültesi", i, ". Ogrencisi:",name)

    else:
        i-=2
        print("Tıp Fakültesi", i , ". Ogrencisi:",name)

#-----------
# enumerate kullanmadan çözümü:

for i in range(len(ogrenciler)):
    if i < 3:
        print("Mühendislik Fakültesi", i+1 , ". Ogrencisi:", ogrenciler[i])

    else:
        print("Tıp Fakültesi", i-2 , ". Ogrencisi:", ogrenciler[i])



###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

#Kredisi ...  olan ...  kodlu dersin kontenjanı ... kişidir."

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

# list(zip(kredi,ders_kodu,kontenjan))
# zip(kredi,ders_kodu,kontenjan)

for krd,kod,kont in zip(kredi,ders_kodu,kontenjan):
    print(f"Kredisi {krd}  olan {kod}  kodlu dersin kontenjanı {kont} kişidir.")

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################
# Bizden beklenen farkını yazdırmak:

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

#Fonksiyon:

def kumeler(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


kumeler(kume1,kume2)







