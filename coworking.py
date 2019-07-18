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
# hitung luas lantai total
luas_lantai_total = org*luas_org # meter persegi

# hitung jumlah keramik
luas_keramik_solo = ... # meter persegi
jumlah_keramik = ... # jumlah

# hitung jumlah bata dari luas tembok total (4 sisi), dikurangi pintu dan jendela
# hitung luas pintu
luas_pintu = ... # meter persegi

# hitung luas jendela
luas_jendela = ... # meter persegi

# hitung luas tembok asli
panjang_sisi_tembok = ... # meter
luas_tembok_total = ... # meter persegi
luas_tembok_asli = luas_tembok_total - jumlah_pintu*luas_pintu - jumlah_jendela*luas_jendela # meter persegi

# hitung jumlah bata
luas_bata_solo = ... # meter persegi
jumlah_bata = ... # jumlah

# estimasi harga
harga_bata_solo = ...
harga_keramik_solo = ...
profit = ...

# hitung harga bangunan
harga_bata_total = ...
harga_keramik_total = ...
harga_bangunan = harga_bata_total + harga_keramik_total

# hitung harga jual
harga_jual = ... # berapa yang harus kamu jual agar tidak rugi? agar mendapatkan keuntungan?


print("===========================================================================================")
print('Jumlah bata yang dibutuhkan: '+str(jumlah_bata))
print('Jumlah keramik yang dibutuhkan: '+str(jumlah_keramik))
print('Harga total yang harus dibayar: '+str(harga_jual))                      

print("================================Thanks For Using COWORKING!================================")