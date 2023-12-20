class Animal:
    def __init__(self, nama, makanan, habitat, reproduksi):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.reproduksi = reproduksi

    def makan(self):
        print(f"{self.nama} sedang makan {self.makanan}")

    def hidup(self):
        print(f"{self.nama} hidup di {self.habitat}")

    def berkembang_biak(self):
        print(f"{self.nama} berkembang biak melalui {self.reproduksi}")


class Badak(Animal):
    def __init__(self, nama, habitat):
        super().__init__(nama, "rumput", habitat, "berkawin")
        self.ukuran_cula = 0

    def tumbuh_cula(self, ukuran):
        self.ukuran_cula += ukuran
        print(f"Cula {self.nama} sekarang berukuran {self.ukuran_cula} inci")


class Ikan(Animal):
    def __init__(self, nama, habitat):
        super().__init__(nama, "plankton", habitat, "bertelur")
        self.jumlah_sirip = 2

    def berenang(self):
        print(f"{self.nama} sedang berenang dengan {self.jumlah_sirip} sirip")


class Ular(Animal):
    def __init__(self, nama, habitat):
        super().__init__(nama, "rodentia", habitat, "bertelur")
        self.panjang = 0

    def tumbuh(self, panjang):
        self.panjang += panjang
        print(f"{self.nama} sekarang memiliki panjang {self.panjang} inci")


# Contoh penggunaan:
badak = Badak("Badak Jawa", "padang rumput")
badak.makan()
badak.hidup()
badak.berkembang_biak()
badak.tumbuh_cula(5)

ikan = Ikan("Ikan Nemo", "laut")
ikan.makan()
ikan.hidup()
ikan.berkembang_biak()
ikan.berenang()

ular = Ular("Ular Sanca", "hutan")
ular.makan()
ular.hidup()
ular.berkembang_biak()
ular.tumbuh(10)
