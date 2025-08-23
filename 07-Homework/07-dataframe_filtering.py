import pandas as pd

sozluk = {
    "Kategori": ["Giyim", "Giyim", "Ayakkabı", "Aksesuar", "Ayakkabı", "Giyim", "Aksesuar", "Aksesuar", "Ayakkabı", "Giyim"],
    "Ürün": ["T-shirt", "T-shirt", "Sandalet", "Küpe", "Spor Ayakkabı", "Pantolon", "Kolye", "Yüzük", "Çizme", "Ceket"],
    "Fiyat": [130, 80, 240, 150, 1200, 300, 600, 250, 2000, 500]
}

df = pd.DataFrame(sozluk)

# 1. Sadece ürün bilgisi (tek sütun)
print(df["Ürün"])

# 2. Sadece kategori bilgisi
print(df["Kategori"])

# 3. Sadece fiyat bilgisi
print(df["Fiyat"])

# 4. Tüm bilgiler (ürün, fiyat, kategori)
print(df)

# 5. 1. ve 3. indeksteki ürünler
print(df.iloc[[1, 3]])

# 6. 2. indeksteki ürün
print(df.iloc[2])

# 7. Sadece ürün bilgisi
print(df["Ürün"])

# 8. Giyim kategorisindeki ürünler
print(df[df["Kategori"] == "Giyim"])

# 9. Ayakkabı kategorisindeki ürünler
print(df[df["Kategori"] == "Ayakkabı"])

# 10. Aksesuar kategorisindeki ürünler
print(df[df["Kategori"] == "Aksesuar"])

# 11. Giyim kategorisinde 300'den fazla olan ürünler
print(df[(df["Kategori"] == "Giyim") & (df["Fiyat"] > 300)])

# 12. Aksesuar kategorisinde fiyatı 600'den az olan ürünler
print(df[(df["Kategori"] == "Aksesuar") & (df["Fiyat"] < 600)])