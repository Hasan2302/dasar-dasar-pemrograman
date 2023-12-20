buah_awal = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_terbalik = [buah for buah in reversed(buah_awal)]
print(buah_terbalik)

buah_awal = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
buah_duplicated = [buah for buah in buah_awal for _ in range(2)]
print(buah_duplicated)

kalimat_awal = "Nurul Fikri"
konsonan = ''.join([karakter for karakter in kalimat_awal if karakter.isalpha() and karakter.lower() not in ['a', 'e', 'i', 'o', 'u']])
print(konsonan)
