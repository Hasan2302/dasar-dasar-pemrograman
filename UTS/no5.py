angka1 = float(input("Masukkan angka 1: "))

angka2 = float(input("Masukkan angka 2: "))

operator = input("Pilih operator (+, -, *, /, **): ")

hasil = 0
keterangan_operator = ""

if operator == '+':
    hasil = angka1 + angka2
    keterangan_operator = "Tambah"
elif operator == '-':
    hasil = angka1 - angka2
    keterangan_operator = "Kurang"
elif operator == '*':
    hasil = angka1 * angka2
    keterangan_operator = "Kali"
elif operator == '/':
    hasil = angka1 / angka2
    keterangan_operator = "Bagi"
elif operator == '**':
    hasil = angka1 ** angka2
    keterangan_operator = "Pangkat"
else:
    print("Operator tidak valid. Program berhenti.")

print("\nAngka pertama:", angka1)
print("Angka kedua:", angka2)
print("Pilihan Operator:", keterangan_operator)
print(f"Hasil operator {angka1} {operator} {angka2} = {hasil}")
