# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Menghitung Luas Ruang")
print("Masukkan Panjang Ruang")
panjang = float(input())
print("Masukkan Lebar Ruang")
lebar = float(input())
print("Masukkan Satuan Meter atau Inci")
satuan = input()
if satuan == "Meter":
    luas = panjang * lebar
    print("Luas Ruang Adalah", luas, "Meter")
elif satuan == "Inci":
    luas = panjang * lebar * 39.37
    print("Luas Ruang Adalah", luas, "Inci")
else:
    print("Satuan Tidak Dikenali")
