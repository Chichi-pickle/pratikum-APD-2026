import os

accounts = [
    ["knight", "123", "Admin"],
    ["chiikawa", "123", "Pengguna"]
]

adventures = [
            ["A001", "Mencabut Rumput Liar / Weed Pulling", "Pekerjaan Utama (Buruh Harian)", "Hutan", 2, 100, "Available"],
            ["A002", "Penaklukan Monster / Monster Hunting", "Pekerjaan Utama (Buruh Harian)", "Hutan sampai Gua", 5, 1000, "Available"],
            ["A003", "Menempel Stiker / Stickering Lemons", "Pekerjaan Sampingan & Paruh Waktu", "Pabrik", 1, 80, "Available"],
            ["A004", "Memetik Jamur / Mushroom Picking", "Pekerjaan Sampingan & Paruh Waktu", "Hutan", 3, 100, "Available"],
            ["A005", "Pegawai Kedai Ramen", "Profesional & Layanan Jasa", "Kedai Ramen", 4, 800, "Available"],
            ["A006", "Pengatur Lalu Lintas / Polisi", "Profesional & Layanan Jasa", "Jalan Raya", 4, 900, "Available"],
            ]
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def input_angka(pesan, minimum):
    while True:
        nilai = input(pesan)

        if nilai.isdigit() and int(nilai) >= minimum:
            return int(nilai)

        print("Input harus berupa angka yang valid!")

def register():
    print("\n========== REGISTER ==========")

    username = input("Buat Username: ")

    if username == "":
        print("Username tidak boleh kosong!")
        return

    for akun in accounts:
        if akun[0] == username:
            print("Username sudah digunakan!")
            return

    password = input("Buat Password: ")

    if password == "":
        print("Password tidak boleh kosong!")
        return

    akun_baru = [username, password, "Pengguna"]
    accounts.append(akun_baru)

    print("Registrasi berhasil!")

def login():
    print("\n========== LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    for akun in accounts:
        if akun[0] == username and akun[1] == password:
            print(f"Login berhasil! Selamat datang {username}")
            return akun
        
    print("Username atau password salah!")
    return None

def pilih_kategori():
    print("\n1. Pekerjaan Utama (Buruh Harian)")
    print("2. Pekerjaan Sampingan & Paruh Waktu")
    print("3. Profesional & Layanan Jasa")

    pilihan = input("Pilih Kategori (1-3): ")
    if pilihan == "1":
        return "Pekerjaan Utama (Buruh Harian)"
    elif pilihan == "2":
        return "Pekerjaan Sampingan & Paruh Waktu"
    elif pilihan == "3":
        return "Profesional & Layanan Jasa"
    
    print("Kategori tidak tersedia!")
    return None

def tambah_adventure():
    print("\n========== ADD ADVENTURE ==========")

    id_adventure = input("ID Adventure: ").strip()

    if id_adventure == "":
        print("ID tidak boleh kosong!")
        return

    for job in adventures:
        if job[0] == id_adventure:
            print("ID Adventure sudah digunakan!")
            return

    nama = input("Nama Adventure: ")

    if nama == "":
        print("Nama Adventure tidak boleh kosong!")
        return

    kategori = pilih_kategori()

    if kategori is None:
        return

    lokasi = input("Lokasi: ")

    if lokasi == "":
        print("Lokasi tidak boleh kosong!")
        return

    kesulitan = input_angka("Tingkat Kesulitan (1-5): ", 1)

    if kesulitan > 5:
        print("Kesulitan hanya boleh 1 sampai 5!")
        return

    reward = input_angka("Reward: ", 0)

    job_baru = [
        id_adventure, nama, kategori, lokasi,
        kesulitan, reward, "Available"
    ]

    adventures.append(job_baru)
    print("Adventure berhasil ditambahkan!")

def lihat_adventure():
    print("\n========== ADVENTURE BOARD ==========")

    if len(adventures) == 0:
        print("Belum ada pekerjaan.")
        return
    
    print("1. Semua Pekerjaan")
    print("2. Filter Berdasarkan Kategori")

    pilihan = input("Pilih 1 Atau 2: ")

    kategori_dicari = None

    if pilihan == "2":
        kategori_dicari = pilih_kategori()
        if kategori_dicari is None:
            return
    elif pilihan != "1":
        print("Pilihan tidak tersedia!")
        return

    ditemukan = False

    for job in adventures:
        if kategori_dicari is None or job[2] == kategori_dicari:
            print("-----------------------------------")
            print("ID         :", job[0])
            print("Pekerjaan  :", job[1])
            print("Kategori   :", job[2])
            print("Lokasi     :", job[3])
            print("Kesulitan  :", job[4])
            print("Reward     :", job[5])
            print("Status     :", job[6])

            ditemukan = True

    if not ditemukan:
        print("Belum ada pekerjaan dalam kategori ini.")

def update_adventure():
    print("\n========== UPDATE ADVENTURE ==========")

    id_cari = input("Masukkan ID Adventure: ")

    for job in adventures:
        if job[0] == id_cari:
            print("Adventure ditemukan!")
            print("Kosongkan nama atau lokasi jika tidak ingin mengubahnya.")

            nama = input("Nama Baru: ")
            if nama != "":
                job[1] = nama

            print("Ubah kategori? (y/n)")
            ubah = input("Pilihan: ")

            if ubah == "y":
                kategori = pilih_kategori()
                if kategori is not None:
                    job[2] = kategori

            lokasi = input("Lokasi Baru: ")
            if lokasi != "":
                job[3] = lokasi

            print("Ubah kesulitan (y/n)")
            if input("Pilihan: ") == "y":
                kesulitan = input_angka("Tingkat Kesulitan (1-5): ", 1)

                if 1 <= kesulitan <= 5:
                    job[4] = kesulitan
                else:
                    print("Kesulitan tidak valid; nilai lama dipertahankan.")

            print("Ubah reward (y/n)")
            if input("Pilihan: ") == "y":
                job[5] = input_angka("Reward Baru: ", 0)

            print("Ubah status? (y/n)")
            if input("Pilihan: ").lower() == "y":
                print("1. Available")
                print("2. Unavailable")
                print("3. Taken")
                status = input("Pilih Dari 1 - 3: ")

                if status == "1":
                    job[6] = "Available"
                elif status == "2":
                    job[6] = "Unavailable"
                elif status == "3":
                    job[6] = "Taken"
                else:
                    print("Status tidak valid; status lama dipertahankan.")

            print("Adventure berhasil diperbarui!")
            return

    print("ID Adventure tidak ditemukan!")

def hapus_adventure():
    print("\n========== DELETE ADVENTURE ==========")

    id_cari = input("Masukkan ID Adventure: ")

    for job in adventures:
        if job[0] == id_cari:
            konfirmasi = input("Yakin Ingin Menghapus Pekerjaan Ini? (y/n): ")  

            if konfirmasi == "y":
                adventures.remove(job)
                print("Adventure berhasil dihapus!") 
            else:
                print("Penghapusan dibatalkan.")

            return
    print("ID Adventure tidak ditemukan!")

def menu_admin():
    while True:
        print("\n===== KNIGHT / ADMIN MENU =====")
        print("1. Add Adventure")
        print("2. View Adventure")
        print("3. Edit Adventure")
        print("4. Delete Adventure")
        print("5. Exit")

        pilihan = input("Pilih Dari 1 - 5: ")

        if pilihan == "1":
            tambah_adventure()
        elif pilihan == "2":
            lihat_adventure()
        elif pilihan == "3":
            update_adventure()
        elif pilihan == "4":
            hapus_adventure()
        elif pilihan == "5":
            print("Logout berhasil!")
            break
        else:
            print("\nPilihan tidak tersedia!")

def menu_pengguna(akun):
    while True:
        print("\n===== ADVENTURER MENU =====")
        print("1. Lihat Adventure Board")
        print("2. Logout")

        pilihan = input("Pilih 1 Atau 2: ")

        if pilihan == "1":
            lihat_adventure()
        elif pilihan == "2":
            print("Logout berhasil!")
            break
        else:
            print("\nPilihan tidak tersedia!")

while True:
    clear_terminal()

    print("====================================")
    print("      CHIIKAWA ADVENTURE BOARD")
    print("====================================")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    pilihan = input("Pilih Dari 1 - 3: ")

    if pilihan == "1":
        akun = login()

        if akun is not None:
            if akun[2] == "Admin":
                menu_admin()
            else:
                menu_pengguna(akun)

    elif pilihan == "2":
        register()

    elif pilihan == "3":
        print("See you on the next adventure!")
        break

    else:
        print("Pilihan tidak tersedia!")

    input("\nTekan Enter untuk melanjutkan...")