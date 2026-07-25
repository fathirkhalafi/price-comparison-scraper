# Price Comparison Scraper

Script Python untuk mengambil dan membandingkan data harga produk dari beberapa sumber/kategori secara otomatis.

## Fungsi
- Mengambil nama produk dan harga dari halaman web target
- Menggabungkan data dari lebih dari satu sumber sekaligus
- Menyimpan hasil ke file CSV yang siap dibuka di Excel/Google Sheets
- (Opsional) Filter produk berdasarkan rentang harga tertentu

## Tech Stack
- Python 3
- `requests` — mengambil HTML dari halaman web
- `BeautifulSoup` — parsing dan ekstraksi data dari HTML
- `csv` — menyimpan hasil dalam format tabel

## Cara Pakai
1. Install dependency:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Edit bagian URL di dalam script sesuai target yang ingin di-scrape
3. Jalankan script:
   ```bash
   python perbandingan_harga.py
   ```
4. Hasil akan tersimpan otomatis sebagai `perbandingan_harga.csv`

## Contoh Output

<img width="1514" height="905" alt="Tangkapan Layar 2026-07-26 pukul 06 57 45" src="https://github.com/user-attachments/assets/fc7cf7cb-a8ec-46aa-89a8-5186ea19334c" />



## Use Case
Script ini cocok digunakan untuk:
- Monitoring harga kompetitor secara berkala
- Riset harga pasar sebelum menentukan harga jual produk
- Mengumpulkan data produk dari beberapa kategori/toko untuk dibandingkan

## Catatan
Script ini dibuat untuk keperluan pembelajaran dan dapat disesuaikan (custom selector, filter, jumlah sumber) sesuai kebutuhan proyek nyata.
