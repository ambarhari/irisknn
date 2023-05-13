# Tugas Kuliah

ini adalah tugas kuliah pak Rahmadya

## catatan

dari tugas asli yang di video ada beberapa perubahan

- php diganti jadi FastApi + uvicorn (karena sekalian percobaan)
- semua form diganti ke template menggunakan multipart
-

## Penggunaan

- clone repository ini
- masuk ke direktori
- ketik:

```
pip install -r requirements.txt
```

- lalu ketik

```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

- untuk dokumentasi via swagger bisa diketik url "localhost:8080/docs"
