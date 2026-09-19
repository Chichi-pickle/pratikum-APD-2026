barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]

total_belanjaan = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
pajak = 0.15 * total_belanjaan
total_bayar = total_belanjaan + pajak

rata_rata = total_bayar / len(barang)

nim = "06"
boolean = int(nim) < rata_rata

total_bayar_usd = total_bayar / 17750
total_bayar_eur = total_bayar / 20350

barang_slicing = barang[0:5:2]

print("Daftar Harga Barang                      :", barang)
print("Total Belanjaan Sebelum Pajak            : Rp", total_belanjaan)
print("Pajak Koperasi 15%                       : Rp", pajak)
print("Total Harga Yang Harus Dibayar           : Rp", total_bayar)
print("Rata-rata Harga Barang                   : Rp", rata_rata)
print("2 Digit NIM                              :", nim)
print("Apakah NIM < Rata-Rata?                  :", boolean)
print("Daftar Harga Barang 1, 3, 5 (Slicing)    :", barang_slicing)
print("Total Harga Yang Harus Dibayar dalam USD : $", total_bayar_usd)
print("Total Harga Yang Harus Dibayar dalam EUR : €", total_bayar_eur)