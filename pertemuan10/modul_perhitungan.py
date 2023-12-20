import math

def operasi_tambah(a, b):
    return a + b

def operasi_kurang(a, b):
    return a - b

def operasi_pangkat(a):
    return a**2

def operasi_kali(a, b):
    return a * b

def operasi_bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol"

def operasi_akar(a):
    return math.sqrt(a)

def operasi_log(angka):
    return math.log(angka)

def operasi_sin(sudut):
    return math.sin(math.radians(sudut))

def operasi_cos(sudut):
    return math.cos(math.radians(sudut))

def operasi_tan(sudut):
    return math.tan(math.radians(sudut))