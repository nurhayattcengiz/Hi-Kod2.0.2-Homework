# DataFrame Filtering with Pandas

This project demonstrates how to create a pandas DataFrame from a Python dictionary and apply various filtering operations based on index, category, and price.

# Dataset Structure

The dataset is defined as a dictionary with three keys:

- `Kategori`: Product category (e.g., Giyim, Ayakkabı, Aksesuar)
- `Ürün`: Product name (e.g., T-shirt, Pantolon, Kolye)
- `Fiyat`: Product price in Turkish Lira (₺)

```python
sozluk = {
    "Kategori": [...],
    "Ürün": [...],
    "Fiyat": [...]
}
