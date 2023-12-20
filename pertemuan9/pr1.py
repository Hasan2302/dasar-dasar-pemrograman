hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

siswa_lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]

print(siswa_lulus)
