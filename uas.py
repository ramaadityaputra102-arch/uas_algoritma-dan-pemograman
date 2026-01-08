# Program Menghitung dan Konversi Nilai Mahasiswa

def hitung_nilai():
    print("--- Program Konversi Nilai Mahasiswa ---")
    
    # Input data dari pengguna
    try:
        absen = float(input("Masukkan Nilai Kehadiran (0-100): "))
        tugas = float(input("Masukkan Nilai Tugas (0-100): "))
        uts   = float(input("Masukkan Nilai UTS (0-100): "))
        uas   = float(input("Masukkan Nilai UAS (0-100): "))

        # Langkah 1: Menghitung Nilai Akhir berdasarkan bobot
        total_nilai = (absen * 0.10) + (tugas * 0.20) + (uts * 0.30) + (uas * 0.40)

        # Langkah 2: Menentukan Nilai Huruf dengan Logika Percabangan
        if total_nilai >= 80:
            huruf = "A"
        elif total_nilai >= 66:
            huruf = "B"
        elif total_nilai >= 56:
            huruf = "C"
        elif total_nilai >= 40:
            huruf = "D"
        else:
            huruf = "E"

        # Langkah 3: Menampilkan Hasil
        print("-" * 40)
        print(f"Total Nilai Akhir: {total_nilai:.2f}")
        print(f"Predikat Nilai   : {huruf}")
        print("-" * 40)

    except ValueError:
        print("Error: Harap masukkan angka yang valid!")

# Menjalankan fungsi
hitung_nilai()