panjang = float (input("Masukkan panjang persegi panjang: "))
lebar = float (input("Masukkan lebar persegi panjang: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas persegi panjang adalah: {luas:g} m2")
print(f"Keliling persegi panjang adalah: {keliling:g} m")

# Trace Table

# Move | Panjang | Lebar | Luas | Keliling
#  1   | 8.00    |   -   |   -  |    -
#  2   | 8.00    | 5.00  |   -  |    -
#  3   | 8.00    | 5.00  | 40.0 |    -
#  4   | 8.00    | 5.00  | 40.0 |   26.0
