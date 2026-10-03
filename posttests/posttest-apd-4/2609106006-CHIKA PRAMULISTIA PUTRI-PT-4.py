username = "chika"
password = "006"
pin_benar = password + password

saldo = 5000000.0

print("=" * 60)
print("        SELAMAT DATANG DI APLIKASI BANK SAWIT JAYA       ")
print("=" * 60)

kesempatan_login = 3
login_sukses = False
blokir_akun = False

while kesempatan_login > 0:
    username_input = input("\nMasukkan Username: ")
    password_input = input("Masukkan Password: ")

    if username_input == username and password_input == password:
        print("\n[SUKSES] Login berhasil! Halo Juragan Sawit!")
        login_sukses = True
        break
    else:
        kesempatan_login -= 1
        if username_input != username and password_input == password:
            print("Username Anda Salah.")
        elif username_input == username and password_input != password:
            print("Password Anda Salah.")
        else:
            print("Username Dan Password Anda Salah.")

        if kesempatan_login > 0:
            print(f"Sisa Kesempatan Login: {kesempatan_login}x Lagi.")
        else:
            print("\n[DIBLOKIR] Anda Telah Gagal Login Sebanyak 3x. Akun diblokir!")
            blokir_akun = True

while login_sukses and not blokir_akun:
    print("\n" + "=" * 60)
    print("                      MENU UTAMA BANK                   ")
    print("=" * 60)
    print("1. Transfer Uang")
    print("2. Logout (Keluar)")
    print("=" * 60)

    pilihan = input("Masukkan pilihan menu (1/2): ")

    if pilihan == "2":
        print("\nTerima Kasih Telah Menggunakan Bank Sawit Jaya. Bye!")
        break
    elif pilihan == "1":
        transfer_lagi = "y"

        while transfer_lagi.lower() == "y":
            print("\n" + "-" * 60)
            print("                   PROSES TRANSFER UANG                ")
            print("-" * 60)
            print(f"Saldo Saat Ini: Rp {saldo:,}")

            penerima = input("Masukkan Username Penerima: ")

            while True:
                nominal = float(input("Masukkan Nominal Transfer: "))

                if nominal < 50000:
                    print("[ERROR] Transfer Gagal! Nominal Minimal Adalah Rp50.000,00.")
                elif nominal > saldo:
                    print("[ERROR] Transfer Gagal! Nominal Melebihi Saldo Tersedia Saat Ini.")
                elif nominal > 1000000:
                    print("[ERROR] Transfer Gagal! Nominal Maksimal Adalah Rp1.000.000,00.")
                else:
                    break

            kesempatan_pin = 3
            pin_sukses = False

            while kesempatan_pin > 0:
                pin_input = input("Masukkan PIN Konfirmasi (6 Digit): ")
                if pin_input == pin_benar:
                    pin_sukses = True
                    break
                else:
                    kesempatan_pin -= 1
                    print(f"[ERROR] PIN Salah! Sisa Kesempatan: {kesempatan_pin}x.")

            if not pin_sukses:
                print("\n[DIBLOKIR] Anda Gagal Memasukkan PIN 3x. Akun diblokir!")
                blokir_akun = True
                break

            saldo -= nominal
            print("\n" + "=" * 60)
            print("                   STRUK BUKTI TRANSFER                     ")
            print("=" * 60)
            print(f"Pengirim    :   {username}")
            print(f"Penerima    :   {penerima}")
            print(f"Nominal     :   Rp {nominal:,}")
            print("Status      :   Berhasil")
            print("=" * 60)

            transfer_lagi = input("\nApakah Anda Ingin Melakukan Transfer Lagi? (y/n): ")
        
        if blokir_akun:
            break
    else:
        print("\n[PILIHAN TIDAK VALID] Silakan Masukkan Angka 1 Atau 2 Saja!") 