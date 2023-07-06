#Görev1

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)


#Görev2

text = "The goal is to turn data into information, and information into insight."

text.upper().replace("."," ").replace(",", " ").split()


#Görev3

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

#1

len(lst)

#2

lst[0]
lst[10]

#3

list(lst[:4])

#4

lst.pop(8)
lst

#5

lst.append("Y")
lst

#6

lst.insert(8,"N")
lst


#Görev4

dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

#1

dict.keys()

#2

dict.values()

#3

dict["Daisy"][1] = 13
dict

#4

dict["Ahmet"] = ["Turkey", "24"]
dict

#5

dict.pop("Antonio")
dict


#Görev5

l = [2, 13, 18, 93, 22]


def func(liste):
     tek = []
     cift = []
     for i in liste:
          if i % 2 == 0:
              cift.append(i)
          else:
               tek.append(i)
     return tek, cift


func(l)

#Görev6

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,o in enumerate(ogrenciler, 1):
     if i <= 3:
          print(f"Mühendislik Fakültesi {i} . öğrenci: {o}")
     else:
          print(f"Tıp Fakültesi {i-3} . öğrenci: {o}")


#Görev7

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu, kredi, kontenjan))

for dk, kredi, kon in zip(ders_kodu, kredi, kontenjan):
     print(f"Kredisi {kredi} olan {dk} kodlu dersin kontenjanı {kon} kişidir")


#Görev8

kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])


def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)
