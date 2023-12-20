import modul_bangun_datar as mbd

import modul_perhitungan as mp

print("Luas Lingkaran:", mbd.hitung_luas_dan_keliling_lingkaran(4)) 
print("Keliling Lingkaran:", mbd.hitung_luas_dan_keliling_lingkaran(4)[1])
print("Luas Segitiga:", mbd.hitung_luas_dan_keliling_segitiga(2, 3, 4)[0])
print("Keliling Segitiga:", mbd.hitung_luas_dan_keliling_segitiga(1, 2, 3)[1])
print("Luas Persegi:", mbd.hitung_luas_dan_keliling_persegi(5)[0]) 
print("Keliling Persegi:", mbd.hitung_luas_dan_keliling_persegi(5)[1])
print("Luas Persegi Panjang:", mbd.hitung_luas_dan_keliling_persegi_panjang(4, 5)[0])
print("Keliling Persegi Panjang:", mbd.hitung_luas_dan_keliling_persegi_panjang(4, 5)[1])
print("Luas Jajar Genjang:", mbd.hitung_luas_dan_keliling_jajargenjang(5, 6, 7)[0])
print("Keliling Jajar Genjang:", mbd.hitung_luas_dan_keliling_jajargenjang(5, 6, 7)[1])
print("Luas Belah Ketupat:", mbd.hitung_luas_dan_keliling_belahketupat(5, 2, 6)[0])
print("Keliling Belah Ketupat:", mbd.hitung_luas_dan_keliling_belahketupat(5, 2, 6)[1])
print("Luas Trapesium:", mbd.hitung_luas_dan_keliling_trapesium(4, 1, 2, 3, 4)[0])
print("Keliling Trapesium:", mbd.hitung_luas_dan_keliling_trapesium(4, 1, 2, 3, 4)[1])

print("Tambah:", mp.operasi_tambah(2, 3))
print("Kurang:", mp.operasi_kurang(9, 7))
print("Pangkat:", mp.operasi_pangkat(4))
print("Kali:", mp.operasi_kali(2, 3))
print("Bagi:", mp.operasi_bagi(8, 2))
print("Akar:", mp.operasi_akar(9))
print("Log:", mp.operasi_log(4))
print("Sin:", mp.operasi_sin(2))
print("Cos:", mp.operasi_cos(5))
print("Tan:", mp.operasi_tan(7))