class Gempa:
    jumlah_gempa = 0 

    def __init__(self, lokasi, magnitudo):
        self.lokasi = lokasi
        self.magnitudo = magnitudo
        Gempa.jumlah_gempa += 1

    def dampak(self):
        if self.magnitudo < 2:
            return "Dampak gempa tidak berasa"
        elif 2 <= self.magnitudo < 4:
            return "Dampak gempa bangunan retak-retak"
        elif 4 <= self.magnitudo < 6:
            return "Dampak gempa bangunan roboh"
        else:
            return "Dampak gempa bangunan roboh dan berpotensi tsunami"
