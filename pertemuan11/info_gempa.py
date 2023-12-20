from gempa import *
banten = Gempa ("Banten",1.2)
palu = Gempa ("Palu", 6.1)
cianjur = Gempa ("Cianjur", 5.6) 
jayapura = Gempa ("Jayapura", 3.3)
garut = Gempa ("Garut", 4.0)

print(f"Gempa di {banten.lokasi} - Magnitudo: {banten.magnitudo}")
print(banten.dampak())

print(f"\nGempa di {palu.lokasi} - Magnitudo: {palu.magnitudo}")
print(palu.dampak())

print(f"\nGempa di {cianjur.lokasi} - Magnitudo: {cianjur.magnitudo}")
print(cianjur.dampak())

print(f"\nGempa di {jayapura.lokasi} - Magnitudo: {jayapura.magnitudo}")
print(jayapura.dampak())

print(f"\nGempa di {garut.lokasi} - Magnitudo: {garut.magnitudo}")
print(garut.dampak())

print(f"\nTotal Gempa yang terjadi: {Gempa.jumlah_gempa}")