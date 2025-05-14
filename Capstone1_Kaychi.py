barang = {
    "Kode Barang" : ['Brg001', 'Brg002', 'Brg003', 'Brg004', 'Brg005', 'Brg006'],
    "Nama Barang" : ['Beras', 'Tepung Terigu', 'Minyak Goreng', 'Kecap Manis', 'Telur', 'Garam'],
    "Stock" : [100, 50, 50, 30, 100, 20],
    "Harga Pokok" : [18500, 13000, 20000, 4000, 2000, 2500],
    "Harga Jual" : [20000, 15000, 22000, 5000, 2500, 3500],}

headerListBarang = ["Kode Barang", "Nama Barang", "Stock", "Harga Pokok", "Harga Jual"]
daftarPenjualan = [
    {"Tanggal": "01-05-2025", "Nama Barang": "Minyak Goreng", "Jumlah": 5},
    {"Tanggal": "01-05-2025", "Nama Barang": "Beras", "Jumlah": 10},
    {"Tanggal": "01-05-2025", "Nama Barang": "Tepung Terigu", "Jumlah": 3},
    {"Tanggal": "02-05-2025", "Nama Barang": "Minyak Goreng", "Jumlah": 3},
    {"Tanggal": "02-05-2025", "Nama Barang": "Beras", "Jumlah": 7},
    {"Tanggal": "02-05-2025", "Nama Barang": "Tepung Terigu", "Jumlah": 5},
    {"Tanggal": "03-05-2025", "Nama Barang": "Minyak Goreng", "Jumlah": 5},
    {"Tanggal": "03-05-2025", "Nama Barang": "Beras", "Jumlah": 10},
    {"Tanggal": "03-05-2025", "Nama Barang": "Tepung Terigu", "Jumlah": 3}]
         
from tabulate import tabulate
## Fungsi menu 1
def stockBarang():
    print("\nBerikut daftar barang yang tersedia")
    print(tabulate(barang, tablefmt="fancy_grid", headers=headerListBarang))

## Fungsi login
def login():
    while True:
        username = input("\nMasukkan user name: ")
        password = input("\nMasukkan password anda: ")
        if username == "user" and password == "123":
            print("\nLogin berhasil!")
            break
        else:
            print("User name atau password tidak sesuai. Silakan coba lagi.")

##Fungsi menu utama
def menuUtama():
    print(f'''\nSelamat datang di Toko Berkah Jaya.\n
          Silakan pilih menu:
          1. Tampilkan Stock Barang
          2. Tambah Stock Barang
          3. Perbarui Daftar Barang
          4. Hapus Barang
          5. Daftar Penjualan
          6. Keluar''')

## FUngsi menu opsi untuk kembali ke menu utama di setiap sub-menu
def menuOpsi():
    while True:
        print(f'''\n
          1. Lanjutkan Program
          2. Keluar
          ''')
        try: 
            opsi = int(input("Masukkan menu yang ingin dipilih: "))
            if opsi == 1:
                return True  # kembali ke menu utama
            elif opsi == 2:
                print("Program selesai. Untuk kembali, silakan log in ulang.")
                return False
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("\nMasukkan hanya angka positif!")

## Fungsi tambah stock untuk menu no. 2
def tambahBarang():
    def inputBarang():
        while True:
            tambahNamaBarang = input("Masukkan nama barang yang ingin ditambahkan: ").title()
            if tambahNamaBarang in barang['Nama Barang']:
                print("\nNama barang sudah tersedia.")
            elif not tambahNamaBarang.isalpha():
                print("\nNama barang hanya boleh berupa huruf.")
            else:
                break
        
        tambahKodeBarang = f"Brg{len(barang['Kode Barang']) + 1:03d}"
        
        while True:
            try:
                tambahStock = int(input("Masukkan jumlah stock: "))
                if tambahStock < 0:
                    print(f"Stock harus lebih dari 0!")
                else:
                    break
            except ValueError:
                print("\nMasukkan hanya angka!")
        while True:
            try:
                tambahHargaPokok = int(input(f"Masukkan harga pokok barang {tambahNamaBarang}: "))
                tambahHargaJual = int(input(f"Masukkan harga jual barang {tambahNamaBarang}: "))
                break
            except ValueError:
                print(f"Harga harus berupa angka!")

        barang['Nama Barang'].append(tambahNamaBarang)
        barang['Kode Barang'].append(tambahKodeBarang)
        barang['Stock'].append(tambahStock)
        barang['Harga Pokok'].append(tambahHargaPokok)
        barang['Harga Jual'].append(tambahHargaJual)
        print(f"\n{tambahNamaBarang} berhasilkan ditambahkan dengan kode barang {tambahKodeBarang}.")
        stockBarang()

    inputBarang()
    while True:
        tambahLagi = input("\nIngin tambahkan barang yang lain? (ya/tidak): ").lower()
        if tambahLagi == 'ya':
            inputBarang()
        elif tambahLagi == 'tidak':
            stockBarang()
            break
        else:
            print("\nInput yang dimasukkan tidak sesuai.")

## Fngsi hapus barang untuk menu no. 4
def hapusBarang():
    stockBarang()
    def inputHapus():
            while True:
                hapus = input("Masukkan nama barang yang ingin dihapus: ").title()
                if hapus in barang['Nama Barang']:
                    index = barang['Nama Barang'].index(hapus)
                    nama = barang['Nama Barang'][index]
                    del barang['Nama Barang'][index]
                    del barang['Kode Barang'][index]
                    del barang['Stock'][index]
                    del barang['Harga Pokok'][index]
                    del barang['Harga Jual'][index]
                    print(f"\n{nama} berhasil dihapus.\n")
                    break
                else:
                    print("Nama barang tidak valid.")

    inputHapus()
    while True:
        hapusLagi = input("\nIngin hapus barang yang lain? (ya/tidak): ").lower()
        if hapusLagi == 'ya':
            inputHapus()
        elif hapusLagi == 'tidak':
            stockBarang()
            break
        else:
            print("\nInput yang dimasukkan tidak sesuai.")

# Fungsi perbarui data untuk menu no. 3
def perbaruiData():
    while True:
        print(f'''\nMenu Perbarui Data Barang:
        1. Perbarui Stock
        2. Perbarui Harga Pokok dan Harga Jual
        3. Kembali ke Menu Utama''')
        try:
            pilihan = int(input("Masukkan pilihan menu: "))
            if pilihan == 1:
                perbaruiStock()
            elif pilihan == 2:
                perbaruiHarga()
            elif pilihan == 3:
                break  # kembali ke menu utama
            else:
                print("Pilihan tidak tersedia. Silakan pilih antara 1 dan 3.")
        except ValueError:
            print("Input harus berupa angka.")

def perbaruiStock():
    stockBarang()
    while True:
        nama = input("Masukkan nama barang yang ingin diperbarui stock-nya: ").title()
        if nama in barang['Nama Barang']:
            try:
                index = barang['Nama Barang'].index(nama)
                stock_baru = int(input(f"Masukkan jumlah stock baru untuk {nama}: "))
                barang['Stock'][index] = stock_baru
                print(f"Stock untuk {nama} berhasil diperbarui menjadi {stock_baru}.")
            except ValueError:
                print("Stock harus berupa angka.")
        else:
            print("Nama barang tidak ditemukan. Silakan coba lagi.")

        # tanya apakah ingin perbarui stock lain
        lanjut = input("\nIngin perbarui stock barang lain? (ya/tidak): ").lower()
        if lanjut != "ya":
            break

def perbaruiHarga():
    stockBarang()
    while True:
        nama = input("Masukkan nama barang yang ingin diperbarui harganya: ").title()
        if nama in barang['Nama Barang']:
            try:
                index = barang['Nama Barang'].index(nama)
                harga_pokok_baru = int(input(f"Masukkan harga pokok baru untuk {nama}: "))
                harga_jual_baru = int(input(f"Masukkan harga jual baru untuk {nama}: "))
                barang['Harga Pokok'][index] = harga_pokok_baru
                barang['Harga Jual'][index] = harga_jual_baru
                print(f"Harga pokok dan harga jual untuk {nama} berhasil diperbarui.")
            except ValueError:
                print("Harga harus berupa angka.")
        else:
            print("Nama barang tidak ditemukan. Silakan coba lagi.")

        # tanya apakah ingin perbarui harga lain
        lanjut = input("\nIngin perbarui harga barang lain? (ya/tidak): ").lower()
        if lanjut != "ya":
            break

# Fungsi tampilkan penjualan untuk menu no. 5
def tampilkanPenjualan():
    print("\nBerikut daftar penjualan\n")
    print(tabulate(daftarPenjualan, tablefmt="fancy_grid", headers="keys"))
    
    while True:
        cari = input("\nIngin menampilkan penjualan berdasarkan nama barang? (ya/tidak): ").lower()
        if cari == 'ya':
            pilihan = input(f"\nMenu Pencarian. Masukkan nama barang: ").title()
            hasilCari = [d for d in daftarPenjualan if d['Nama Barang'] == pilihan]
            if hasilCari:
                print(f"\nBerikut hasil pencarian untuk {pilihan}\n")
                print(tabulate(hasilCari, tablefmt="fancy_grid", headers="keys"))
            else:
                print(f"\nTidak ada data penjualan untuk barang: {pilihan}")
        elif cari == 'tidak':
            break
        else:
            print("\nPilihan yang dimasukkan tidak valid.")

# Alur tampilan menu
while True:
    print("\nSelamat datang!")
    login()
    lanjut = True
    while True:
        menuUtama()
        try:
            menu = int(input("\nSilakan masukkan menu yang ingin dijalankan: "))
            if menu == 1:
                stockBarang()
            elif menu == 2:
                stockBarang()
                tambahBarang()
            elif menu == 3:
                perbaruiData()
                continue
            elif menu == 4:
                hapusBarang()
            elif menu == 5:
                tampilkanPenjualan()
            elif menu == 6:
                print("Terima kasih. Anda berhasil keluar")
                lanjut = False
                break
            else:
                print("Menu yang dimasukkan tidak sesuai.")
                continue
        except ValueError:
            print("Masukkan angka yang sesuai dengan menu.")
            continue

        # Hanya tampilkan menuOpsi untuk menu selain 3 dan 6
        if menu not in [3, 6]:
            if not menuOpsi():
                break
