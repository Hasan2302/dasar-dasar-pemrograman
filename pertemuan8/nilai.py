input_nilai = float(input("Masukkan nilai: "))

def NilaiKelulusan(nilai):
    if nilai < 60:
        return "Kurang Baik"
    elif 60 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

hasil = NilaiKelulusan(input_nilai)
print("Hasil: ", hasil)
