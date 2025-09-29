import pandas as pd
import matplotlib.pyplot as plt

# 1.CSV dosyasını oku
file_path = r"C:\Users\nrhtc\OneDrive\Masaüstü\proje_1\archive\Istanbul_BarrageIntakeandConsumption.csv"
df = pd.read_csv(file_path)

# 2. Tarih kolonunu datetime formatına çevir
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# 3. NaT olan satırları çıkar
df = df[df['Date'].notna()]

# 4. En yoğun 10 günü bul
top_days = df.sort_values(by='Total_Consumption', ascending=False).head(10)

# 5. Tablo olarak göster
print(top_days[['Date', 'Total_Consumption']])

# 6. Bar grafikle görselleştir
plt.figure(figsize=(10,5))
plt.bar(top_days['Date'].astype(str), top_days['Total_Consumption'], color='crimson')
plt.title("En Yoğun 10 Gün", fontsize=14)
plt.xlabel("Tarih", fontsize=12)
plt.ylabel("Tüketim (Watt)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Aylık Ortalama Tüketim Analizi:
# Aylık ortalama tüketimi hesapla
monthly_avg = df.groupby(df["Date"].dt.to_period("M"))["Total_Consumption"].mean()

# Index'i zaman serisine çevir
monthly_avg.index = monthly_avg.index.to_timestamp()

# Alan grafiği
plt.figure(figsize=(14,6))
plt.fill_between(monthly_avg.index, monthly_avg.values, color='skyblue', alpha=0.5)
plt.plot(monthly_avg.index, monthly_avg.values, color='navy', linewidth=2)
plt.title("Aylık Ortalama Tüketim (Alan Grafiği)", fontsize=16)
plt.xlabel("Ay", fontsize=12)
plt.ylabel("Tüketim (kWh)", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. Sub-metering Karşılaştırması(barajlar üzerinden):
import seaborn as sns
import matplotlib.pyplot as plt

# Stil ayarı
sns.set_style("whitegrid")

# Baraj kolonları
baraj_kolonlari = ['Omerli', 'Darlik', 'Elmali', 'Terkos', 'B.Cekmece',
                   'Sazlidere', 'Alibey', 'Kazandere', 'Pabucdere', 'Istırancalar']

# Ortalama tüketimi hesapla
baraj_ortalama = df[baraj_kolonlari].mean()

# Bar grafikle görselleştir
plt.figure(figsize=(14,6))
sns.barplot(x=baraj_ortalama.index, y=baraj_ortalama.values, palette='crest')
plt.title("Baraj Bazlı Ortalama Su Tüketimi", fontsize=18)
plt.xlabel("Barajlar", fontsize=12)
plt.ylabel("Ortalama Tüketim (m³)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Tahminleme Modeli:
# Zaman Serisi Formatı:
# 1.CSV dosyasını oku

file_path = r"C:\Users\nrhtc\OneDrive\Masaüstü\proje_1\archive\Istanbul_BarrageIntakeandConsumption.csv"
df = pd.read_csv(file_path)    
    
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True) 

#Tahminleme Modeli: Basit Hareketli Ortalama (Moving Average):
import matplotlib.pyplot as plt

plt.figure(figsize=(14,6))
df['Total_Consumption'].plot(label='Gerçek Tüketim', color='teal')
df['Tahmin'] = df['Total_Consumption'].rolling(window=7).mean()
df['Tahmin'].plot(label='7 Günlük Ortalama', color='orange')
plt.title("Toplam Su Tüketimi ve Hareketli Ortalama", fontsize=16)
plt.xlabel("Tarih", fontsize=12)
plt.ylabel("Tüketim (m³)", fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
    
# Prophet ile Gelecek Su Tüketimi Tahmini (30 Günlük):
from prophet import Prophet
import matplotlib.pyplot as plt

# Prophet formatına uygun veri çerçevesi
df_prophet = df.reset_index()[['Date', 'Total_Consumption']]
df_prophet.columns = ['ds', 'y']

# Prophet modeli
model = Prophet()
model.fit(df_prophet)

# Gelecek 30 gün için tahmin
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Tahmin grafiği
fig = model.plot(forecast)
plt.title("Gelecek 30 Günlük Su Tüketimi Tahmini", fontsize=16)
plt.xlabel("Tarih")
plt.ylabel("Tüketim (m³)")
plt.grid(True)
plt.tight_layout()
plt.show()


#bileşenleri ayrı görmek için.
# model.plot_components(forecast)

# Prophet Tahmininin Doğruluğunu Ölçmek:
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Prophet formatına uygun veri çerçevesi
df_prophet = df.reset_index()[['Date', 'Total_Consumption']]
df_prophet.columns = ['ds', 'y']

# Prophet modeli
model = Prophet()
model.fit(df_prophet)

# Gelecek 30 gün için tahmin
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Tahmin grafiği
fig = model.plot(forecast)
plt.title("Gelecek 30 Günlük Su Tüketimi Tahmini", fontsize=16)
plt.xlabel("Tarih")
plt.ylabel("Tüketim (m³)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gerçek ve tahmin değerlerini birleştir
df_merged = df_prophet.merge(forecast[['ds', 'yhat']], on='ds')
df_merged.dropna(inplace=True)

# Hata metrikleri
mae = mean_absolute_error(df_merged['y'], df_merged['yhat'])
mse = mean_squared_error(df_merged['y'], df_merged['yhat'])
rmse = np.sqrt(mse)

print(f"MAE (Ortalama Mutlak Hata): {mae:.2f}")
print(f"RMSE (Kök Ortalama Kare Hata): {rmse:.2f}")
# MAE:Prophet’in tahminlerinin ortalama ne kadar saptığını gösterir (m³ cinsinden)
# RMSE:Büyük hatalara daha duyarlı; tahminin ne kadar “dağıldığını” ölçer

# Düşük değerler → iyi tahmin
# Yüksek değerler → modelin iyileştirilmesi gerekebilir

#MAE (Ortalama Mutlak Hata): 67291.51
#RMSE (Kök Ortalama Kare Hata): 94604.96

