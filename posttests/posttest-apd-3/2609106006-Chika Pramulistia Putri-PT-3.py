print("=== SISTEM KASIR BIOSKOP ===")

nama = input("Nama Pembeli: ")
umur = int(input("Umur Pembeli: "))

if umur < 13:
    print("\nMohon maaf, anda belum cukup umur untuk menonton.")
else:
    jenis_tiket = input("Jenis tiket (Reguler / Premium / VIP): ")

    if jenis_tiket not in ["Reguler", "Premium", "VIP"]:
        print("\n[PERINGATAN] Jenis tiket tidak valid! Transaksi dibatalkan.")
    else:
        if jenis_tiket == "Reguler":
            harga_tiket = 50000
        elif jenis_tiket == "Premium":
            harga_tiket = 75000
        else:
            harga_tiket = 100000

        member = input("Status member (Ya / Tidak): ")
        
        diskon_persen = 0.20 if member == "Ya" else 0.0
        nominal_diskon = harga_tiket * diskon_persen

        biaya_admin = 0 if member == "Ya" else 2000

        total_bayar = int(harga_tiket - nominal_diskon + biaya_admin)

        print(f"Total yang harus dibayar: Rp {total_bayar:,}")
        uang_bayar = int(input("Nominal uang bayar: Rp "))

        if uang_bayar < total_bayar:
            print("\n[PERINGATAN] Uang bayar kurang! Transaksi dibatalkan dan struk tidak dicetak.")
        else:
            kembalian = uang_bayar - total_bayar

            print("\n" + "="*50)
            print("                 STRUK PEMBELIAN                ")
            print("="*50)
            print(f"Nama Pembeli    : {nama}")
            print(f"Umur Pembeli    : {umur} tahun")
            print(f"Jenis Tiket     : {jenis_tiket}")
            print(f"Status Member   : {member}")
            print(f"Harga Tiket     : Rp {harga_tiket:,}")
            print(f"Potongan Diskon : Rp {int(nominal_diskon):,}")
            print(f"Biaya Admin     : Rp {biaya_admin:,}")
            print("="*50)
            print(f"Total Bayar     : Rp {total_bayar:,}")
            print(f"Uang Bayar      : Rp {uang_bayar:,}")
            print(f"Kembalian       : Rp {kembalian:,}")
            print("="*50)
            print("         Terima Kasih & Selamat Menonton!       ")
            print("="*50)