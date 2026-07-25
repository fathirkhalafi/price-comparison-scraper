import requests
from bs4 import BeautifulSoup
import csv

def scrape_produk(url, sumber):
    """Scrape produk dari 1 URL, kasih label 'sumber' biar tau asalnya dari mana"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    produk_list = soup.find_all("div", class_="product-wrapper")
    
    hasil = []
    for p in produk_list:
        nama_tag = p.find("a", class_="title")
        harga_tag = p.find("span", itemprop="price")
        
        if nama_tag and harga_tag:
            nama = nama_tag.get("title")
            harga = harga_tag.text.strip()
            hasil.append({"sumber": sumber, "nama": nama, "harga": harga})
    
    return hasil

# Scrape dari 2 kategori berbeda (anggap ini "toko A" dan "toko B")
laptop = scrape_produk("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops", "Toko Laptop")
tablet = scrape_produk("https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets", "Toko Tablet")

# Gabungin semua data
semua_data = laptop + tablet

print(f"Total data terkumpul: {len(semua_data)}")

# Simpan ke CSV
with open("perbandingan_harga.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=["sumber", "nama", "harga"], delimiter=";")
    writer.writeheader()
    for row in semua_data:
        writer.writerow(row)

print("Data berhasil disimpan ke perbandingan_harga.csv!")