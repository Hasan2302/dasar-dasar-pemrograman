def hitung_luas_dan_keliling_lingkaran(r, phi=22/7):
    luas = phi * r**2
    keliling = 2 * phi * r
    return luas, keliling

def hitung_luas_dan_keliling_segitiga(a, b, c):
    s = (a + b + c) / 2
    luas = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    keliling = a + b + c
    return luas, keliling

def hitung_luas_dan_keliling_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def hitung_luas_dan_keliling_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def hitung_luas_dan_keliling_jajargenjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2 * (alas + sisi_miring)
    return luas, keliling

def hitung_luas_dan_keliling_belahketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    return luas, keliling

def hitung_luas_dan_keliling_trapesium(tinggi, a, b, c, d):
    luas = 0.5 * tinggi * (a + b)
    keliling = a + b + c + d
    return luas, keliling