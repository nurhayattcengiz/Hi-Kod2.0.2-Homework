# 1.SORU:
#x = 3 ----> floata çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
#y = 4.5 -----> integere çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
#z = "8" -----> integera çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
#a = "12" -----> floata çevirelim. Çevirdikten sonra beri tipinide yazdıralım.
#b = "46.8" ------> integera çevirelim. Çevirdikten sonra beri tipinide yazdıralım.

# x = 3 ---> floata çevir
x = 3
x_float = float(x)
print("x:", x_float, "| Type:", type(x_float))

# y = 4.5 ---> integere çevir
y = 4.5
y_int = int(y)
print("y:", y_int, "| Type:", type(y_int))

# z = "8" ---> integera çevir
z = "8"
z_int = int(z)
print("z:", z_int, "| Type:", type(z_int))

# a = "12" ---> floata çevir
a = "12"
a_float = float(a)
print("a:", a_float, "| Type:", type(a_float))

# b = "46.8" ---> integera çevir
b = "46.8"
b_int = int(float(b))  # önce float'a sonra integer'a dönüşüm!
print("b:", b_int, "| Type:", type(b_int))

# 2.SORU:
# Yaş değerleri isimlere atanıyor
ali_age = 23
ayse_age = 27
mehmet_age = 21

# Karşılaştırmalar ve mantıksal operatör kullanımı
# Ayşe Ali'den büyük ve Mehmet'ten de büyük mü?
print("Ayşe herkesten büyük mü?", ayse_age > ali_age and ayse_age > mehmet_age)

# Mehmet en küçük mü ya da Ali ile aynı yaşta mı?
print("Mehmet en küçük ya da Ali ile aynı yaşta mı?", mehmet_age < ali_age or mehmet_age == ali_age)

# Ayşe Ali’den küçük değil mi?
print("Ayşe Ali'den küçük değil:", not ayse_age < ali_age)

# 3.SORU:
# Kullanıcıdan iki sayı alınır
num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))

# Dört işlem uygulanır
print("Toplam:", num1 + num2)
print("Fark:", num1 - num2)
print("Çarpım:", num1 * num2)

# Sıfıra bölme kontrolü
if num2 != 0:
    print("Bölüm:", num1 / num2)
else:
    print("Bölüm: Hata! Sıfıra bölme yapılamaz.")
    
# 4.SORU:
# Kullanıcıdan bilgi alma
name = input("Adınızı girin: ")
age = input("Yaşınızı girin: ")
city = input("Şehrinizi girin: ")
job = input("Mesleğinizi girin: ")

# Alınan bilgileri ekrana yazdırma
print("\n--- Kullanıcı Bilgileri ---")
print("İsim:", name)
print("Yaş:", age)
print("Şehir:", city)
print("Meslek:", job)

# 5.SORU:
# İfade tanımlanır
phrase = "Hi-Kod Veri Bilimi Atölyesi"

# 1. Her kelimeyi ayrı değişkenlere ayır
words = phrase.split()  # boşluklara göre ayırır
word1, word2, word3, word4 = words[0], words[1], words[2], words[3]

print("Kelime 1:", word1)
print("Kelime 2:", word2)
print("Kelime 3:", word3)
print("Kelime 4:", word4)

# 2. Tümünü büyük harfe çevir
upper_phrase = phrase.upper()
print("BÜYÜK HARFLİ İFADE:", upper_phrase)

# 3. Tümünü küçük harfe çevir
lower_phrase = phrase.lower()
print("küçük harfli ifade:", lower_phrase)

# Sayı ifadesi
numbers = "0123456789"

# Yalnızca çift sayıları seç (0, 2, 4, 6, 8)
even_digits = "".join([char for char in numbers if int(char) % 2 == 0])
print("Çift sayılar:", even_digits)

# Yalnızca tek sayıları seç (1, 3, 5, 7, 9)
odd_digits = "".join([char for char in numbers if int(char) % 2 != 0])
print("Tek sayılar:", odd_digits)