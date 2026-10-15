# angka_genap = {2,4,6,8,10}
# angka = {1,2,3,4,5}

# for item in angka:
#     if item == 1 or item == 2:
#         print(item)
# angka.add(4)
# print(angka)
# angka.discard(4)
# print(angka)
# for item in list(angka):
#         if item == 3:
#             angka.remove(3)
# print(angka)
# print(angka_genap.union(angka))
# print(angka_genap | angka)
# print(angka_genap.intersection(angka))
# print(angka_genap & angka)
# print(angka.difference(angka_genap))
# print(angka_genap - angka)

# kendaraan = {
#     'Mobil' : 'Innova', #key = Mobil, Value = Innova
#     'Motor' : 'Vario'
# }
# makanan = {
#     "nasgor" : 15000,
#     "bakso"  : 20000
# }
# menu = "bubur ayam", "papeda", "es teh", "sempol"
# harga = 10000
# makanan = dict.fromkeys(menu, harga)
# print(makanan)
# makanan2 = makanan.copy()
# makanan2["soto"] = 20000
# print(makanan2)
# print("Jumlah Makanan", len(makanan))
# del makanan
# hapus = makanan.pop("bakso")
# makanan.clear()
# print(makanan)
# print(hapus)
# makanan.update({"sate" : 25000, 
#                 "mie ayam" : 15000})
# tambah = makanan.setdefault("bakso", 35000)
# makanan["sate"] = 25000
# for key, value in kendaraan.items():
#     print(f'Key {key} : Value {value}')
# print(kendaraan['Motor'][6]['Angka'][3])
# poli_umum = {"Andi", "Budi", "Citra", "Doni"}
# poli_gigi = {"Citra", "Doni", "Eka", "Fani"}

# print(poli_umum.union(poli_gigi))
