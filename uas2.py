def terbilang(n):
    # b) Deklarasi array/list angka (indeks 0 sengaja dikosongkan "")
    angka = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", 
             "Tujuh", "Delapan", "Sembilan", "Sepuluh", "Sebelas"]
    
    hasil = ""
    n = int(n) # Memastikan input adalah bilangan bulat

    # c) Logika pengkondisian sesuai instruksi
    if n < 12:
        hasil = " " + angka[n]
    elif n < 20:
        hasil = terbilang(n % 10) + " Belas"
    elif n < 100:
        # Menggunakan // untuk pembagian bulat di Python
        hasil = terbilang(n // 10) + " Puluh" + terbilang(n % 10)
    elif n < 200:
        hasil = " Seratus" + terbilang(n % 100)
    elif n < 1000:
        hasil = terbilang(n // 100) + " Ratus" + terbilang(n % 100)
    elif n < 2000:
        hasil = " Seribu" + terbilang(n - 1000)
    elif n < 1000000:
        hasil = terbilang(n // 1000) + " Ribu" + terbilang(n % 1000)
    elif n < 1000000000:
        hasil = terbilang(n // 1000000) + " Juta" + terbilang(n % 1000000)
    else:
        # Untuk angka 1 Milyar ke atas
        hasil = terbilang(n // 1000000000) + " Milyar" + terbilang(n % 1000000000)
        
    return hasil

# a) Tentukan input bilangan
input_angka = int(input("Masukkan angka: "))
print(f"Terbilang: {terbilang(input_angka)}")