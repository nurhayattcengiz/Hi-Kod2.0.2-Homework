import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dosyayı okuyalım
df = pd.read_csv("students_performance.csv")
print(df.head())

# 2. Kadın-erkek sayısına bakalım
print(df["gender"].value_counts())

# 3. Kadın-erkek histogramı
sns.countplot(x="gender", data=df)
plt.title("Gender Distribution")
plt.show()

# 4. Race/Ethnicity sütunundaki grup sayısı
race = df["race/ethnicity"].value_counts()
print(race)

# 5. Race/Ethnicity görselleştirmesi
sns.countplot(x="race/ethnicity", data=df, order=race.index)
plt.title("Race/Ethnicity Distribution")
plt.xticks(rotation=45)
plt.show()

# 6. Parental level of education eşsiz değerler
print(df["parental level of education"].value_counts())

# 7. Lunch sütunundaki eşsiz değerler
print(df["lunch"].unique())

# 8. Lunch türlerine göre kişi sayısı
print(df["lunch"].value_counts())

# 9. Gender’a göre ortalama skorlar
print(df.groupby("gender")[["math score", "reading score", "writing score"]].mean())

# 10. Race/Ethnicity’e göre ortalama skorlar
print(df.groupby("race/ethnicity")[["math score", "reading score", "writing score"]].mean())

# 11. Parental level of education’a göre ortalama skorlar
print(df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean())

# 12. Lunch türlerine göre ortalama skorlar
print(df.groupby("lunch")[["math score", "reading score", "writing score"]].mean())

# 13. Test preparation course’a göre ortalama skorlar
print(df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean())