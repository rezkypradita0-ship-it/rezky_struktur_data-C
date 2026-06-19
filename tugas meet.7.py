# SOAL:
#Deskripsi Tugas
#Buatlah sebuah program sederhana menggunakan bahasa pemrograman Python yang menerapkan konsep list. Program yang dibuat adalah Aplikasi Manajemen Nilai Mahasiswa.

#Ketentuan Program:
#Menampilkan daftar data mahasiswa.
#Menambahkan data mahasiswa baru.
#Mengubah data mahasiswa.
#Menghapus data mahasiswa.
#Mencari data mahasiswa berdasarkan nama.
#Mengurutkan data mahasiswa berdasarkan nilai tertinggi.
#Menghitung rata-rata nilai mahasiswa.
#Keluar dari program.

#Program wajib menggunakan list sebagai tempat penyimpanan data.
#Contoh struktur data:

#data_mahasiswa = [
#    ["Ahmad", 85],
#    ["Budi", 78],
#    ["Citra", 90]
#]

#Setiap data mahasiswa disimpan dalam bentuk list seperti berikut:
#["Nama Mahasiswa", Nilai]

#Contoh Tampilan Menu Program

#Program yang dibuat minimal memiliki tampilan menu seperti berikut:

#====================================
# APLIKASI MANAJEMEN NILAI MAHASISWA
#====================================
#1. Tampilkan Data
#2. Tambah Data
#3. Ubah Data
#4. Hapus Data
#5. Cari Data
#6. Urutkan Data Berdasarkan Nilai
#7. Hitung Rata-rata Nilai
#8. Keluar

#Pilih menu 1-8:


# JAWAB:

# Inisialisasi data awal (Trik: Taruh angka NILAI di depan agar mudah di-.sort)
data_mahasiswa = [
    [100, "nabila"],
    [78, "alifa"],
    [90, "putri"]
]

while True:
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA ")
    print("====================================")
    print("1. Tampilkan Data\n2. Tambah Data\n3. Ubah Data\n4. Hapus Data")
    print("5. Cari Data\n6. Urutkan Berdasarkan Nilai\n7. Hitung Rata-rata\n8. Keluar")
    print("====================================")
    
    pilihan = input("Pilih menu 1-8: ")
    print("------------------------------------")

    # 1. TAMPILKAN DATA
    if pilihan == "1":
        if len(data_mahasiswa) == 0:
            print("Data mahasiswa masih kosong!")
        else:
            print("No | Nama Mahasiswa       | Nilai")
            print("------------------------------------")
            for i in range(len(data_mahasiswa)):
                # data_mahasiswa[i][1] adalah Nama, data_mahasiswa[i][0] adalah Nilai
                print(f"{i+1}  | {data_mahasiswa[i][1]:<20} | {data_mahasiswa[i][0]}")

    # 2. TAMBAH DATA
    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa baru: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        # Disimpan dengan format [nilai, nama]
        data_mahasiswa.append([nilai, nama])
        print(f"Data {nama} berhasil ditambahkan!")

    # 3. UBAH DATA
    elif pilihan == "3":
        nama_cari = input("Masukkan nama mahasiswa yang ingin diubah: ")
        ketemu = False
        
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][1].lower() == nama_cari.lower():
                nama_baru = input("Masukkan nama baru: ")
                nilai_baru = int(input("Masukkan nilai baru: "))
                data_mahasiswa[i] = [nilai_baru, nama_baru]
                print("Data berhasil diubah!")
                ketemu = True
                break
        if not ketemu:
            print("Data tidak ditemukan.")

    # 4. HAPUS DATA
    elif pilihan == "4":
        nama_hapus = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        ketemu = False
        
        for mhs in data_mahasiswa:
            if mhs[1].lower() == nama_hapus.lower():
                data_mahasiswa.remove(mhs)
                print(f"Data {nama_hapus} berhasil dihapus!")
                ketemu = True
                break
        if not ketemu:
            print("Data tidak ditemukan.")

    # 5. CARI DATA
    elif pilihan == "5":
        nama_cari = input("Masukkan nama mahasiswa yang dicari: ")
        ketemu = False
        
        for mhs in data_mahasiswa:
            if mhs[1].lower() == nama_cari.lower():
                # Menampilkan indeks menggunakan fungsi .index() sesuai materi gambar pertama
                indeks = data_mahasiswa.index(mhs)
                print(f"Data Ditemukan di indeks {indeks} -> Nama: {mhs[1]}, Nilai: {mhs[0]}")
                ketemu = True
                break
        if not ketemu:
            print("Mahasiswa tidak ditemukan.")

    # 6. URUTKAN DATA (Sangat Sederhana Menggunakan Materi .sort & .reverse)
    elif pilihan == "6":
        if len(data_mahasiswa) == 0:
            print("Data kosong, tidak bisa diurutkan.")
        else:
            # Karena angka nilai berada di depan (indeks 0), .sort() otomatis mengurutkan berdasarkan nilai
            data_mahasiswa.sort()
            data_mahasiswa.reverse() # Dibalik agar dari yang terbesar
            print("Data berhasil diurutkan! Silakan cek menu 1 untuk melihat hasilnya.")

    # 7. HITUNG RATA-RATA NILAI
    elif pilihan == "7":
        if len(data_mahasiswa) == 0:
            print("Data kosong, rata-rata nilai adalah 0.")
        else:
            total_nilai = 0
            for mhs in data_mahasiswa:
                total_nilai += mhs[0] # mhs[0] adalah nilai
                
            rata_rata = total_nilai / len(data_mahasiswa)
            print(f"Total Mahasiswa : {len(data_mahasiswa)}")
            print(f"Rata-rata Nilai : {rata_rata:.2f}")

    # 8. KELUAR
    elif pilihan == "8":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid!")






