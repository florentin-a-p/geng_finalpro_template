# FINAL PROJECT Q1 - FINTECH COMPANY
# Generation Girl Summer Club 2019 - Computer Science 101 - Bahasa Class
# Mentors: Florentin Anggraini Purnama

# Developer 1:
# Developer 2:


print("========================================FINTECH=========================================")
print("[Sign Up]")

nama = ...
print(...) # Halo, <nama!>! Selamat datang di FINTECH!


# cek validitas nomor HP
# asumsikan selalu ada input dan input nomor HP akan selalu positif
no_hp = input(...) 

minta = True
while (minta):
    if ( ((...) or (...)) and ((...) and (...)) ):  # jika nomor HP valid
        minta = False # keluar dari loop dan pergi ke langkah selanjutnya
    else: # jika nomor HP tidak valid
        minta = True 
        no_hp = ... # tetap minta nomor HP ke user


# cek validitas nomor KTP
# asumsikan selalu ada input dan input nomor KTP akan selalu positif
# asumsikan jenis kelaminnya selalu benar
no_ktp = # minta user memasukkan nomor KTP
jenis_kelamin = # minta user memasukkan jenis kelamin


# masukkan daftar kode wilayah menggunakan list
daftar_kode_wilayah = [[...,...], 
                       [...,...], 
                       [...,...], 
                       [...,...], 
                       .
                       .
                       .]

minta = True 
while (minta):
    if ( ... ): # jika nomor KTP valid
        minta = False # keluar dari loop dan pergi ke langkah selanjutnya
    else: # jika nomor KTP tidak valid
        minta = True
        no_hp = ... # tetap minta nomor KTP ke user

# cek_provinsi
for kode in daftar_kode_wilayah: # bandingkan semua kode wilayah dalam daftar dengan kode wilayah di KTP
    if ... == ... : # jika menemukan kode wilayah yang cocok di daftar kode wilayah
        provinsi = ...  # masukkan provinsi sesuai kode wilayah

# cek tanggal lahir
if jenis_kelamin == 'P': # jika jenis kelamin perempuan
    tanggal_lahir = ... - 400000 # ambil kode tanggal lahir pada KTP
    tanggal_lahir = str(tanggal_lahir) 
elif jenis_kelamin == 'L':  # jika jenis kelamin laki-laki
    tanggal_lahir = ...


print("Terima kasih atas registrasinya! Kamu lahir di "+provinsi+" dan pada tanggal "+tanggal_lahir+" ya?")
print("================================Thanks For Using FINTECH!================================")