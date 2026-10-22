# def luas_persegi():
#     sisi = 2
#     luas = sisi*sisi
#     return luas

# def luas_persegi():
#     sisi = 2
#     luas = sisi*sisi
#     print(luas)

# luas = luas_persegi()
# print(luas)

# kamu = "Kamu Global"
# def kamu():
#     print("Kamu di sini")

# print(kamu)

# def sapa(a = 'andi'):
#     print(f"halo {a}")

# sapa('budi')

# def start(jumlah):
#     for i in range(jumlah):
#         print("Hello")

# mulai = start(5)

# def faktorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * faktorial(n - 1)
# print(faktorial(0))

def luas(sisi):
    luas = sisi ** 2
    return luas
while True:
    try:
        sisi = int(input("Masukkan Nilai Sisi: "))
        if sisi == 0:
            raise ValueError("sisi bernilai 0")
    except ValueError as e:
        print(e)
        continue
    finally:
        print("Blok Kode djalan sekali")
    print(luas(sisi))
    break
