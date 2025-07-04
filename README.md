# Cheque Manager

Aplikasi manajemen stok cek dan giro berbasis web menggunakan Flask dan MySQL.

## 📦 Fitur

- Menambah data stok cek bank
- Menampilkan daftar cek
- Menandai dan mengeluarkan cek secara massal (bulk action)
- Validasi otomatis nomor awal dan akhir
- Tampilan responsif dengan Tailwind CSS dan Alpine.js

---

## 🛠️ Instalasi

### Clone repositori ini
```bash
git clone https://github.com/BangEjak04/bank-transaction.git
cd bank-transaction
```

### Install NPM
```bash
npm install
```

### Buat python virtual environment
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### Jalankan Project
```bash
python app.py
```

Lalu buka: http://127.0.0.1:5000