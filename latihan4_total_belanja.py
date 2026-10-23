barang = input("Masukkan Nama Barang: ")
harga = int(input("Masukkan Harga Satuan Barang: "))
jumlah = int(input("Masukkan Jumlah Barang: "))

subtotal = harga * jumlah
ppn = subtotal * 0.11
total = subtotal + ppn

print(f"Nama Barang: {barang}")
print(f"Jumlah Barang: {jumlah}")
print(f"Subtotal: Rp {subtotal:,.2f}")
print(f"PPN (11%): Rp {ppn:,.2f}")
print(f"Total: Rp {total:,.2f}")