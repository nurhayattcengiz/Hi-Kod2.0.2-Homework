# 1.SORU:
# Kullanıcıdan maaş bilgisi alınır
salary = float(input("Lütfen maaşınızı girin: "))

# Gelir düzeyine göre vergi oranı belirlenir
if salary <= 10000:
    tax_rate = 0.05
elif salary <= 25000:
    tax_rate = 0.10
elif salary <= 45000:
    tax_rate = 0.25
else:
    tax_rate = 0.30

# Kesinti hesaplanır
tax_amount = salary * tax_rate
new_salary = salary - tax_amount

# Sonuç ekrana yazdırılır
print(f"\nVergi oranı: %{tax_rate * 100}")
print(f"Kesinti tutarı: {tax_amount:.2f} TL")
print(f"Yeni maaşınız: {new_salary:.2f} TL")

# 2.SORU:
# Kullanıcıdan kullanıcı adı ve şifre alınır
username = input("Kullanıcı adınızı girin: ")
password = input("Şifrenizi oluşturun: ")

# Şifre uzunluğu kontrol edilir
if len(password) >= 6:
    print("Hesabınız oluşturuldu.")
else:
    print("Şifreniz en az 6 karakter olmalıdır. Lütfen tekrar deneyin.")
    
# 3.SORU:
# Kullanıcıdan geçerli bir şifre alana kadar döngü devam eder
while True:
    password = input("Şifrenizi oluşturun (5-10 karakter arası): ")
    
    # Şifre uzunluğu kontrolü
    if 5 <= len(password) <= 10:
        print("Hesabınız oluşturuldu.")
        break  # Döngüyü sonlandır
    else:
        print("Lütfen girdiğiniz şifre 5 haneden az 10 haneden fazla olmasın!")
        
# 4.SORU:
# Önceden tanımlı şifre
correct_password = "12345"

# Kullanıcıdan isim alınır
username = input("Kullanıcı adınızı girin: ")

# Şifre için 3 deneme hakkı tanımlanır
attempts = 3

# Doğru şifre girilene veya haklar bitene kadar döngü çalışır
while attempts > 0:
    password = input("Şifrenizi girin: ")
    
    if password == correct_password:
        print(f"Giriş yapıldı. Hoş geldin, {username}!")
        break
    else:
        attempts -= 1
        print("Yanlış şifre girildi!")
        if attempts > 0:
            print(f"Kalan deneme hakkınız: {attempts}")
        else:
            print("3 kez yanlış girildi, program sonlandırılıyor.")