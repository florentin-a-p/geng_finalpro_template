# FINAL PROJECT Q2 - COWORKING COMPANY
# Generation Girl Summer Club 2019 - Computer Science 101 - Bahasa Class
# Mentors: Florentin Anggraini Purnama

# Developer 1:
# Developer 2:

print("========================================COWORKING=========================================")
print("[Sign Up]")

nama = ... # Halo, <nama!>! Selamat datang di COWORKING!
print(...) 

# input 
org = int(input(...))

jumlah_pintu = float(input(...))
panjang_pintu = float(input(...))
lebar_pintu = float(input(...))

jumlah_jendela = float(input(...))
panjang_jendela = float(input(...))
lebar_jendela = float(input(...))

# asumsikan ruangan dan keramik berbentuk persegi
# asumsikan tidak ada kursi dan meja di ruangan
# estimasi ukuran
luas_org = ... # meter persegi
tinggi_tembok = ... # meter
panjang_bata = ... # meter
lebar_bata = ... # meter
sisi_keramik = ... # meter

# hitung jumlah keramik dari luas lantai
def hitung_luas_lantai_total(...):
    luas_lantai_total = org*luas_org # meter persegi
    return luas_lantai_total

def hitung_jumlah_keramik(...,...,...):
    luas_keramik_solo = sisi_keramik**2 # meter persegi
    jumlah_keramik = luas_lantai_total/luas_keramik_solo # jumlah
    return jumlah_keramik

# hitung jumlah bata dari luas tembok total (4 sisi), dikurangi pintu dan jendela
def hitung_luas_pintu(...,...):
    luas_pintu = panjang_pintu * lebar_pintu # meter persegi
    return luas_pintu

def hitung_luas_jendela(...,...):
    luas_jendela = panjang_jendela * lebar_jendela # meter persegi
    return luas_jendela

def hitung_luas_tembok_asli(...):
    panjang_sisi_tembok = luas_lantai_total**(1/2) # meter
    luas_tembok_total = panjang_sisi_tembok * tinggi_tembok # meter persegi
    luas_tembok_asli = luas_tembok_total - jumlah_pintu*luas_pintu - jumlah_jendela*luas_jendela # meter persegi
    return luas_tembok_asli

def hitung_jumlah_bata(...,...,...):
    luas_bata_solo = panjang_bata*lebar_bata # meter persegi
    jumlah_bata = luas_tembok_asli/luas_bata_solo # jumlah
    return jumlah_bata

# run all the functions
luas_lantai_total = hitung_luas_lantai_total(...)
jumlah_keramik = hitung_jumlah_keramik(...,...,...)
luas_pintu = hitung_luas_pintu(...,...)
luas_jendela = hitung_luas_jendela(...,...)
luas_tembok_asli = hitung_luas_tembok_asli(...)
jumlah_bata = hitung_jumlah_bata(...,...,...)

print("===========================================================================================")
print('Jumlah bata yang kamu butuhkan: '+str(jumlah_bata))
print('Jumlah keramik yang kamu butuhkan: '+str(jumlah_keramik))
                      
print("================================Thanks For Using COWORKING!================================")