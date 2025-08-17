# Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur.
# Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.
#Sözlük üzerinde değerleri değiştirme, yeni değer ekleme.
# kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın

# Öğrenci notlarını tutan sözlük
ogrenciler = {
    "Ahmet": {"Matematik": 85, "Fizik": 78, "Kimya": 92},
    "Ayşe": {"Matematik": 90, "Fizik": 88, "Kimya": 95},
    "Mehmet": {"Matematik": 70, "Fizik": 65, "Kimya": 80}
}

def not_goster(isim, ders):
    if isim in ogrenciler:
        if ders in ogrenciler[isim]:
            print(f"{isim} adlı öğrencinin {ders} notu: {ogrenciler[isim][ders]}")
        else:
            print(f"{ders} dersi bulunamadı.")
    else:
        print(f"{isim} adlı öğrenci bulunamadı.")

def not_guncelle(isim, ders, yeni_not):
    if isim in ogrenciler:
        ogrenciler[isim][ders] = yeni_not
        print(f"{isim} adlı öğrencinin {ders} notu {yeni_not} olarak güncellendi.")
    else:
        print(f"{isim} adlı öğrenci bulunamadı.")

def yeni_ogrenci_ekle(isim, notlar):
    if isim not in ogrenciler:
        ogrenciler[isim] = notlar
        print(f"{isim} adlı öğrenci eklendi.")
    else:
        print(f"{isim} zaten mevcut.")

# Kullanıcı etkileşimi
while True:
    print("\n--- Öğrenci Not Sistemi ---")
    print("1. Not Göster")
    print("2. Not Güncelle")
    print("3. Yeni Öğrenci Ekle")
    print("4. Tüm Öğrencileri Göster")
    print("5. Çıkış")
    
    secim = input("Seçiminizi yapın (1-5): ")
    
    if secim == "1":
        isim = input("Öğrenci ismi: ")
        ders = input("Ders ismi (Matematik, Fizik, Kimya): ")
        not_goster(isim, ders)
    
    elif secim == "2":
        isim = input("Öğrenci ismi: ")
        ders = input("Ders ismi: ")
        yeni_not = int(input("Yeni not: "))
        not_guncelle(isim, ders, yeni_not)
    
    elif secim == "3":
        isim = input("Yeni öğrenci ismi: ")
        matematik = int(input("Matematik notu: "))
        fizik = int(input("Fizik notu: "))
        kimya = int(input("Kimya notu: "))
        yeni_ogrenci_ekle(isim, {"Matematik": matematik, "Fizik": fizik, "Kimya": kimya})
    
    elif secim == "4":
        for isim, dersler in ogrenciler.items():
            print(f"{isim}: {dersler}")
    
    elif secim == "5":
        print("Programdan çıkılıyor...")
        break
    
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")