import pandas as pd
import matplotlib.pyplot as plt

# Kadın oranı verisi (TÜİK 2024 raporundan alınan örnek değerler)
data = {
    'Bölüm': ['Bilgi Teknolojileri', 'Hematoloji', 'Fen Bilimleri'],
    'Kadın Oranı (%)': [41.3, 21.0, 39.4]
}

# Veri çerçevesi oluştur
df = pd.DataFrame(data)

# Veriyi görüntüle
print("Akademik Alanlara Göre Kadın Temsili:\n")
print(df)

# Bar grafiği oluştur
plt.figure(figsize=(8, 5))
bars = plt.bar(df['Bölüm'], df['Kadın Oranı (%)'], color='mediumorchid', edgecolor='darkviolet')

# Her barın üstüne oranı yaz
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}%', ha='center', color='black', fontsize=10)

# Grafik başlık ve eksenler
plt.title('Akademik Alanlara Göre Kadın Temsili – TÜİK 2024', fontsize=13)
plt.xlabel('Bölüm')
plt.ylabel('Kadın Oranı (%)')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=30)
plt.tight_layout()

# Grafiği göster
plt.show()





