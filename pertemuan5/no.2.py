# nama = ["hasan","udin","sistem","informasi"]
# angka = [1, 2, 3, 4]

# angka.append(5)
# print(angka)

# tambah = nama + angka

# print(tambah)

# cuaca = input ("cuaca hari ini ?")

# match cuaca:
#     case "panas"|"PANAS"|"Panas":
#         print("pakai gojek jangan manja")
#     case "cerah"|"CERAH"|"cerah":
#         print("BERANGKAT!!")
#     case "hujan"|"HUJAN"|"Hujan":
#         print("pakai go car!!")
#     case _:
#         print("UDAH NGAMPUS AJA SIH!!")

ket  = '''
selamat datang diaplikasi perhitungan
silahkan pilih menu yang akan anda jalankan
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
'''
pilihan = input(ket)

match pilihan:
    case "1":
        print("kamu memilih 2 untuk menghitung luas persegi")
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas_persegi = sisi * sisi

        print("Luas persegi:", luas_persegi)
    case "2":
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari = float(input("Masukkan jari-jari lingkaran: "))
        luas =3.14*jari*jari

        print("Luas lingkaran:", luas)
    case "3":
        print("kamu memilih 2 untuk menghitung luas segitiga")
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas_segitiga = 0.5 * alas * tinggi

        print("Luas segitiga:", luas_segitiga)
    case _:
        print("salah pilih")