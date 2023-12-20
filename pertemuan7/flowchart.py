# Input Nama Kendaraan, Jenis Bensin, dan Kota Tujuan
nama_kendaraan = input("Nama kendaraan: ")
jenis_bensin = input("Jenis bensin (Pertalite, Pertamax, Pertamax Turbo): ")
kota_tujuan = input("Kota tujuan (Jakarta, Bekasi, Depok, Tangerang, Bogor): ")

# Menentukan harga dan jarak tempuh berdasarkan jenis bensin
if jenis_bensin == "Pertalite":
    harga_per_liter = 10000
    jarak_tempuh = 12
elif jenis_bensin == "Pertamax":
    harga_per_liter = 14000
    jarak_tempuh = 13
elif jenis_bensin == "Pertamax Turbo":
    harga_per_liter = 17000
    jarak_tempuh = 13.5
else:
    print("Jenis bensin tidak valid")
    exit()

# Menentukan jarak kota berdasarkan kota tujuan
if kota_tujuan == "Jakarta":
    jarak_kota = 20
elif kota_tujuan == "Bekasi":
    jarak_kota = 35.7
elif kota_tujuan == "Depok":
    jarak_kota = 5
elif kota_tujuan == "Tangerang":
    jarak_kota = 99
elif kota_tujuan == "Bogor":
    jarak_kota = 120.6
else:
    print("Kota tujuan tidak valid")
    exit()

# Menghitung pemakaian bensin dan total harga
pemakaian_bensin = jarak_kota / jarak_tempuh
total_harga = pemakaian_bensin * harga_per_liter

# Menampilkan output
print("\nNama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota Tujuan:", kota_tujuan)
print("Pemakaian Bensin:", pemakaian_bensin, "liter")
print("Total Harga:", total_harga, "rupiah")
