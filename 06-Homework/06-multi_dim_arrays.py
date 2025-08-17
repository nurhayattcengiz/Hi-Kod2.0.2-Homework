import numpy as np

# 1 Tek Boyutlu Integer Array Oluşturma
tek_boyutlu = np.array([3, 7, 1, 9, 4], dtype=int)
print("1 Tek Boyutlu Array:", tek_boyutlu)
print("Boyut (ndim):", tek_boyutlu.ndim)
print("Eleman sayısı (size):", tek_boyutlu.size)
print("Şekil (shape):", tek_boyutlu.shape)

# 2 İki ve Üç Boyutlu Array Oluşturma
iki_boyutlu = np.array([[1, 2, 6, 7],
                        [4, 3, 9, 5]])

uc_boyutlu = np.array([[[7, 5, 14], [21, 8, 11]],
                       [[8, 6, 20], [14, 3, 9]]])

print("İki Boyutlu Array:")
print(iki_boyutlu)
print("Boyut:", iki_boyutlu.ndim)
print("Eleman sayısı:", iki_boyutlu.size)
print("Şekil:", iki_boyutlu.shape)

print("Üç Boyutlu Array:")
print(uc_boyutlu)
print("Boyut:", uc_boyutlu.ndim)
print("Eleman sayısı:", uc_boyutlu.size)
print("Şekil:", uc_boyutlu.shape)

# 3 Indexleme İşlemleri
print("Indexleme:")
print("İki boyutlu arraydeki 2:", iki_boyutlu[0][1])
print("İki boyutlu arraydeki 7:", iki_boyutlu[0][3])
print("Üç boyutlu arraydeki 9:", uc_boyutlu[1][1][2])
print("Üç boyutlu arraydeki 5:", uc_boyutlu[0][0][1])

# 4 Slicing İşlemleri
print("Slicing:")
print("2 ve 6:", iki_boyutlu[0, 1:3])
print("3,9,5:", iki_boyutlu[1, 1:])
print("21,8,11:", uc_boyutlu[0][1])
print("6,20:", uc_boyutlu[1][0][1:3])

# 5 Sıfır ve Birlerden Oluşan Arrayleri Birleştirme
zeros_array = np.zeros((5, 3), dtype=int)
ones_array = np.ones((5, 3), dtype=int)

print("Sıfır Array:", zeros_array)
print("Bir Array:", ones_array)

vertical_merge = np.vstack((zeros_array, ones_array))
print("Satır Bazında Birleştirme:", vertical_merge)

horizontal_merge = np.hstack((zeros_array, ones_array))
print("Sütun Bazında Birleştirme:", horizontal_merge)

