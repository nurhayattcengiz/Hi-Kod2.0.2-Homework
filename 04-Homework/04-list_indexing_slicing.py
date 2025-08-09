#Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.

#liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

#"3" değerine ulaşmak için indexleme yapın.

#"Hi-Kod" değerine ulaşmak için indexleme yapın.

#4.7 değerine ulaşmak için indexleme yapın.

#9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.

#8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.

#Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

#liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

#Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.

#for index in range(len(meyveler)):

#   print("{}. indexte bulunan meyve: {}".format(index,meyveler[index])

# 1.SORU:
# Liste üzerinde indexing ve slicing:
liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]

# 2.SORU:
# String Veri Tiplerini Ayıklama:
yeni_liste = []

for eleman in liste:
    if type(eleman) == str:
        yeni_liste.append(eleman)

print(yeni_liste)

# 3.SORU:
# Enumerate Kullanımı:
meyveler = ["Elma", "Muz", "Kiraz", "Portakal"]

for index, meyve in enumerate(meyveler):
    print("{}. indexte bulunan meyve: {}".format(index, meyve))

