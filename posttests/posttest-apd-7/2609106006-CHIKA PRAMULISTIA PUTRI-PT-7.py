import os

nama_program = "CHIIKAWA ADVENTURE BOARD"

accounts = {
    "knight": {"password": "123", "role": "Admin"},
    "chiikawa": {"password": "123", "role": "Pengguna"}
}

adventures = {
    "A001": {"nama": "Mencabut Rumput Liar / Weed Pulling", "kategori": "Pekerjaan Utama (Buruh Harian)", "lokasi": "Hutan", "kesulitan": 2, "reward": 100, "status": "Available"},
    "A002": {"nama": "Penaklukan Monster / Monster Hunting", "kategori": "Pekerjaan Utama (Buruh Harian)", "lokasi": "Hutan sampai Gua", "kesulitan": 5, "reward": 1000, "status": "Available"},
    "A003": {"nama": "Menempel Stiker / Stickering Lemons", "kategori": "Pekerjaan Sampingan & Paruh Waktu", "lokasi": "Pabrik", "kesulitan": 1, "reward": 80, "status": "Available"},
    "A004": {"nama": "Memetik Jamur / Mushroom Picking", "kategori": "Pekerjaan Sampingan & Paruh Waktu", "lokasi": "Hutan", "kesulitan": 3, "reward": 100, "status": "Available"},
    "A005": {"nama": "Pegawai Kedai Ramen", "kategori": "Profesional & Layanan Jasa", "lokasi": "Kedai Ramen", "kesulitan": 4, "reward": 800, "status": "Available"},
    "A006": {"nama": "Pengatur Lalu Lintas / Polisi", "kategori": "Profesional & Layanan Jasa", "lokasi": "Jalan Raya", "kesulitan": 4, "reward": 900, "status": "Available"},
}

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def input_angka(pesan, minimum):
    while True:
        try:
            nilai = int(input(pesan))

            if nilai < minimum:
                print(f"Angka minimal adalah {minimum}!")
                continue

            return nilai

        except ValueError:
            print("Input harus berupa angka yang valid!")

def cari_adventure(id_adventure):
    return adventures.get(id_adventure.strip().upper())

def hitung_reward_rekursif(daftar_reward):
    if len(daftar_reward) == 0:
        return 0
    return daftar_reward[0] + hitung_reward_rekursif(daftar_reward[1:])

def tampilkan_total_reward():
    daftar_reward = [job["reward"] for job in adventures.values()]
    total_reward = hitung_reward_rekursif(daftar_reward)
    print(f"Total reward seluruh adventure: {total_reward}")

def register():
    clear_terminal()
    print("\n========== REGISTER ==========")

    username = input("Buat Username: ")

    if not username:
        print("Username tidak boleh kosong!")
        return

    if username in accounts:
        print("Username sudah digunakan!")
        return

    password = input("Buat Password: ")
    if not password:
        print("Password tidak boleh kosong!")
        return

    accounts[username] = {"password": password, "role": "Pengguna"}
    print("Registrasi berhasil!")

def login():
    clear_terminal()
    print("\n========== LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    akun = accounts.get(username)

    if akun is not None and akun["password"] == password:
        print(f"Login berhasil! Selamat datang, {username}.")
        return {"username": username, **akun}
        
    print("Username atau password salah!")
    return None

def pilih_kategori():
    print("\n1. Pekerjaan Utama (Buruh Harian)")
    print("2. Pekerjaan Sampingan & Paruh Waktu")
    print("3. Profesional & Layanan Jasa")

    pilihan = input("Pilihan (1-3): ").strip()

    kategori = {
        "1": "Pekerjaan Utama (Buruh Harian)",
        "2": "Pekerjaan Sampingan & Paruh Waktu",
        "3": "Profesional & Layanan Jasa"
    }

    if pilihan not in kategori:
        print("Kategori tidak tersedia!")
        return None

    return kategori[pilihan]

def tambah_adventure():
    print("\n========== ADD ADVENTURE ==========")

    id_adventure = input("ID Adventure: ").strip().upper()

    if not id_adventure:
        print("ID tidak boleh kosong!")
        return

    if id_adventure in adventures:
        print("ID Adventure sudah digunakan!")
        return

    nama = input("Nama Adventure: ")

    if not nama:
        print("Nama Adventure tidak boleh kosong!")
        return

    kategori = pilih_kategori()

    if kategori is None:
        return

    lokasi = input("Lokasi: ")

    if not lokasi:
        print("Lokasi tidak boleh kosong!")
        return

    kesulitan = input_angka("Tingkat Kesulitan (1-5): ", 1)
    if kesulitan > 5:
        print("Kesulitan hanya boleh 1 sampai 5!")
        return

    reward = input_angka("Reward: ", 0)

    adventures[id_adventure] = {
        "nama": nama,
        "kategori": kategori,
        "lokasi": lokasi,
        "kesulitan": kesulitan,
        "reward": reward,
        "status": "Available"
    }
    print("Adventure berhasil ditambahkan!")

def lihat_adventure():
    print("\n========== ADVENTURE BOARD ==========")

    if not adventures:
        print("Belum ada pekerjaan.")
        return
    
    print("1. Semua Pekerjaan")
    print("2. Filter Berdasarkan Kategori")
    print("3. Lihat Total Reward")

    pilihan = input("Pilih 1 - 3: ")

    if pilihan == "3":
        tampilkan_total_reward()
        return
    elif pilihan == "1":
        kategori_dicari = None
    elif pilihan == "2":
        kategori_dicari = pilih_kategori()
        if kategori_dicari is None:
            return
    else:
        print("Pilihan tidak tersedia!")
        return

    ditemukan = False

    for id_adventure, job in adventures.items():
        if kategori_dicari is None or job["kategori"] == kategori_dicari:
            print("-----------------------------------")
            print(f"ID         : {id_adventure}")
            print(f"Pekerjaan  : {job['nama']}")
            print(f"Kategori   : {job['kategori']}")
            print(f"Lokasi     : {job['lokasi']}")
            print(f"Kesulitan  : {job['kesulitan']}")
            print(f"Reward     : {job['reward']}")
            print(f"Status     : {job['status']}")
            ditemukan = True
    if not ditemukan:
        print("Belum ada pekerjaan dalam kategori ini.")

def update_adventure():
    print("\n========== UPDATE ADVENTURE ==========")

    id_cari = input("Masukkan ID Adventure: ").strip().upper()
    job = cari_adventure(id_cari)

    if job is None:
        print("ID Adventure tidak ditemukan!")
        return

    print("Adventure ditemukan!")
    print("Kosongkan nama atau lokasi jika tidak ingin mengubahnya.")

    nama = input("Nama Baru: ")
    if nama != "":
        job["nama"] = nama

    print("Ubah kategori? (y/n)")
    if input("Pilihan: ") == "y":
        kategori = pilih_kategori()
        if kategori is not None:
            job["kategori"] = kategori

    lokasi = input("Lokasi Baru: ")
    if lokasi != "":
        job["lokasi"] = lokasi

    print("Ubah kesulitan (y/n)")
    if input("Pilihan: ") == "y":
        kesulitan = input_angka("Tingkat Kesulitan (1-5): ", 1)
        if 1 <= kesulitan <= 5:
            job["kesulitan"] = kesulitan
        else:
            print("Kesulitan tidak valid; nilai lama dipertahankan.")

    print("Ubah reward (y/n)")
    if input("Pilihan: ") == "y":
        job["reward"] = input_angka("Reward Baru: ", 0)

    print("Ubah status? (y/n)")
    if input("Pilihan: ") == "y":
        print("1. Available")
        print("2. Unavailable")
        print("3. Taken")
        status = input("Pilih Dari 1 - 3: ")

        if status == "1":
            job["status"] = "Available"
        elif status == "2":
            job["status"] = "Unavailable"
        elif status == "3":
            job["status"] = "Taken"
        else:
            print("Status tidak valid; status lama dipertahankan.")

    print("Adventure berhasil diperbarui!")
    return

def hapus_adventure():
    print("\n========== DELETE ADVENTURE ==========")

    id_cari = input("Masukkan ID Adventure: ").strip().upper()
    job = cari_adventure(id_cari)

    if job is None:
        print("ID Adventure tidak ditemukan!")
        return

    print("Yakin Ingin Menghapus Pekerjaan Ini? (y/n): ")
    if input("Pilihan: ") == "y":
        del adventures[id_cari]
        print("Adventure berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

def menu_admin():
    while True:
        print("\n===== KNIGHT / ADMIN MENU =====")
        print("1. Add Adventure")
        print("2. View Adventure")
        print("3. Edit Adventure")
        print("4. Delete Adventure")
        print("5. Exit")

        pilihan = input("Pilih Dari 1 - 5: ")

        try:
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
        except (KeyError, TypeError) as error:
            print(f"Terjadi kesalahan saat mengolah data: {error}")
        except Exception as error:
            print(f"Terjadi kesalahan yang tidak terduga: {error}")
            input("\nTekan Enter untuk melanjutkan...")

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

def main():
    while True:
        clear_terminal()
        print("====================================")
        print(f"      {nama_program}")   
        print("====================================")           
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        pilihan = input("Pilih Dari 1 - 3: ")

        if pilihan == "1":
            akun = login()
            if akun is not None:
                if akun["role"] == "Admin":
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

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan.")
    except Exception as error:
        print(f"Terjadi kesalahan pada program: {error}")