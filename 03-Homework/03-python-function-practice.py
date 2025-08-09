# 1.SORU:
# Daire Alanı Hesaplama Fonksiyonu:
def daire_alani_hesapla(pi_degeri, yaricap):
    """π * r^2 formülüyle dairenin alanını hesaplar"""
    alan = pi_degeri * (yaricap ** 2)
    return alan

# Örnek kullanım:
pi = float(input("π değerini girin: "))
r = float(input("Yarıçapı girin: "))
print("Dairenin alanı:", daire_alani_hesapla(pi, r))

# 2.SORU:
# Faktöriyel Hesaplama Fonksiyonu (format ile yazdırma):
def faktoriyel(n):
    """Girilen sayının faktöriyelini döngü ile hesaplar"""
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    print("Faktöriyel: {}! = {}".format(n, sonuc))
# Örnek kullanım:
sayi = int(input("Bir sayı girin: "))
faktoriyel(sayi)
   
# 3.SORU:
# Yaş Hesaplama Fonksiyonu:
def yas_hesapla(dogum_yili):
    """Doğum yılına göre yaşı hesaplar"""
    mevcut_yil = 2025
    return mevcut_yil - dogum_yili

# Örnek kullanım:
yil = int(input("Doğum yılınızı girin: "))
print("Yaşınız:", yas_hesapla(yil))

# 4.SORU:
# Emeklilik Kontrol Fonksiyonu (Fonksiyon içinde fonksiyon):
def yas_hesapla(dogum_yili):
    """Doğum yılına göre yaşı hesaplar"""
    mevcut_yil = 2025
    return mevcut_yil - dogum_yili

def emeklilik_kontrol(isim, dogum_yili):
    """Kişinin emekli olup olmadığını veya kaç yıl kaldığını hesaplar"""
    yas = yas_hesapla(dogum_yili)
    if yas >= 65:
        return "Emekli oldunuz."
    else:
        kalan_yil = 65 - yas
        return "{} kişinin emekliliğine {} yıl kaldı.".format(isim, kalan_yil)

# Örnek kullanım:
isim_girisi = input("Adınızı girin: ")
dogum_girisi = int(input("Doğum yılınızı girin: "))
print(emeklilik_kontrol(isim_girisi, dogum_girisi))
    

   