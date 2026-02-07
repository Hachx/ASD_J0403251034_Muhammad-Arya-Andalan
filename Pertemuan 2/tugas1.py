nama_file = "stok_barang.txt"

#membuat fungsi membaca stok barang
def baca_data_barang(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open("stok_barang.txt","r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  #menghilang karakter jenis baru
            kode, nama, jumlah = baris.split(",") # pecah menjadi data satuan
            #simpan data dalam dictionary (key value)
            data_dict[kode] = {
                "nama" : nama,
                "jumlah" : int(jumlah)
        }
    return data_dict

#membuat fungsi menampilkan data
def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print("Data Kosong")
        return
    #Membuat Header Tabel
    print('\n============ Stok Barang ============')
    print(f"{'Kode':<10} | {'Nama Barang':<15} | {'Jumlah':>5}" )
    print("-" * 32)
    for kode in sorted(data_dict.keys()):
        nama=data_dict[kode]["nama"]
        jumlah = data_dict[kode]["jumlah"]
        print(f"{kode:<10} | {nama:<15} | {jumlah:>5}")

#membuat fungsi mencari data
def cari_data(data_dict):
    #mencari data barang berdasarkan kode
    kode_cari = input("Masukkan Kode barang yang ingin dicari: ").strip()

    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        jumlah = data_dict[kode_cari]["jumlah"]

        print("\n==== Data Barang Ditemukan ====")
        print(f"Kode     : {kode_cari}")
        print(f"Nama     : {nama}")
        print(f"Jumlah   : {jumlah}")
    else:
        print("\nBarang tidak ditemukan")

#membuat fungsi menambah barang
def tambah_barang(nama_file, data_dict):
    with open(nama_file,"a",encoding="utf-8") as file:
        kode = input('Masukkan kode barang (BRGXXX): ')
        if kode in data_dict:
            print("Kode sudah ada, penambahan gagal")
            return
        nama = input('Masukkan nama barang: ')
        if nama in data_dict:
            print("Kode sudah ada, penambahan gagal")
            return
        jumlah = int(input("Masukkan jumlah stok: "))
        file.write(f"{kode},{nama},{jumlah}\n")

#membuat fungsi update jumlah barang
def update_jumlah_stok(data_dict):
    
    #cari kode barang yang akan diupdate stoknya
    kode = input("Masukkan Kode barang yang akan diupdate stoknya: ").strip()

    if kode not in data_dict:
        print("Kode tidak ditemukan, Update dibatalkan")
        return
    try:
        jumlah_baru = int(input("Masukkan jumlah stok baru:  ").strip())
    except ValueError:
        print('Stok harus berupa angka. Update dibatalkan')
        return
    
    if jumlah_baru < 0:
        print("Jumlah tidak valid. Update dibatalkan")
    else:
        jumlah_lama = data_dict[kode]["jumlah"]
        #memasukkan nilai update terbaru ke dictionary
        data_dict[kode]["jumlah"] = jumlah_baru

        print(f"Update Berhasil, Nilai {kode} barubah dari {jumlah_lama} menjadi {jumlah_baru}")

#membuat fungsi simpan data
def simpan_data(nama_file, data_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            jumlah = data_dict[kode]["jumlah"]
            file.write(f"{kode},{nama},{jumlah}\n")
        
#membuat menu program
def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_barang(nama_file)

    while True:
        print("\n=== MENU STOK BARANG ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan kode")
        print("3. Tambah data baru")
        print("4. Update jumlah stok")
        print("5. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        
        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan == "3":
            tambah_barang(nama_file,buka_data)

        elif pilihan == "4":
            update_jumlah_stok(buka_data)

        elif pilihan == "5":
            simpan_data(nama_file,buka_data)
            print("Data berhsil disimpan")

        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()