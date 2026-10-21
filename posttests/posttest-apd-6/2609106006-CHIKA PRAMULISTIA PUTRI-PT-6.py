import os

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


while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("====================================")
    print("      CHIIKAWA ADVENTURE BOARD")
    print("====================================")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    pilihan = input("Pilih Dari 1 - 3: ")

    if pilihan == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("\n========== LOGIN ==========")

        username = input("Username: ")
        password = input("Password: ")

        if username in accounts and accounts[username]["password"] == password:
            role = accounts[username]["role"]
            print(f"\nLogin berhasil! Selamat datang {username}")
    
            if role == "Admin":
                while True:
                    print("===== KNIGHT / ADMIN MENU =====")
                    print("1. Add Adventure")
                    print("2. View Adventure")
                    print("3. Edit Adventure")
                    print("4. Delete Adventure")
                    print("5. Exit")

                    pilihan = input("Pilih Dari 1 - 5: ")

                    if pilihan == "1":
                        print("\n========== ADD ADVENTURE ==========")
                        
                        id_adventure = input("ID Adventure: ").strip()
                        
                        if id_adventure == "":
                            print("ID tidak boleh kosong!")
                        elif id_adventure in adventures:
                            print("ID Adventure sudah digunakan!")
                        else:
                            nama = input("Nama Adventure: ")
                            if nama == "":
                                print("Nama Adventure tidak boleh kosong!")
                            else:
                                print("\n1. Pekerjaan Utama (Buruh Harian)")
                                print("2. Pekerjaan Sampingan & Paruh Waktu")
                                print("3. Profesional & Layanan Jasa")
                            
                                pilihan = input("Pilih Kategori (1-3): ")

                                kategori = ""
                                if pilihan == "1":
                                    kategori = "Pekerjaan Utama (Buruh Harian)"
                                elif pilihan == "2":
                                    kategori = "Pekerjaan Sampingan & Paruh Waktu"
                                elif pilihan == "3":
                                    kategori = "Profesional & Layanan Jasa"

                                if kategori == "":
                                    print("Kategori tidak tersedia!")
                                else:
                                    lokasi = input("Lokasi: ")
                                    if lokasi == "":
                                        print("Lokasi tidak boleh kosong!")
                                    else:
                                        while True:
                                            kesulitan = input("Tingkat Kesulitan (1-5): ")

                                            if not kesulitan.isdigit():
                                                print("Input harus berupa angka yang valid!")
                                                continue

                                            kesulitan = int(kesulitan)
                                            if kesulitan < 1 or kesulitan > 5:
                                                print("Kesulitan hanya boleh 1 sampai 5!")
                                                continue
                                            break
                                        
                                        while True:
                                            reward = input("Reward: ")

                                            if not reward.isdigit():
                                                print("Input harus berupa angka yang valid!")
                                                continue
                                            reward = int(reward)
                                            break

                                        adventures[id_adventure] = {
                                            "nama" : nama,
                                            "kategori" : kategori,
                                            "lokasi" : lokasi,
                                            "kesulitan" : kesulitan,
                                            "reward" : reward,
                                            "status" : "Available"
                                        }
                                        print("Adventure berhasil ditambahkan!")
                                        
                    
                    elif pilihan == "2":
                        print("\n========== ADVENTURE BOARD ==========")

                        if len(adventures) == 0:
                            print("Belum ada pekerjaan.")
                        else:
                            print("1. Semua Pekerjaan")
                            print("2. Filter Berdasarkan Kategori")

                            pilihan = input("Pilih 1 Atau 2: ")

                            kategori_dicari = ""
                            valid = True
                            if pilihan == "2":
                                print("\n1. Pekerjaan Utama (Buruh Harian)")
                                print("2. Pekerjaan Sampingan & Paruh Waktu")
                                print("3. Profesional & Layanan Jasa")
                            
                                pilihan = input("Pilih Kategori (1-3): ")

                                if pilihan == "1":
                                    kategori_dicari = "Pekerjaan Utama (Buruh Harian)"
                                elif pilihan == "2":
                                    kategori_dicari = "Pekerjaan Sampingan & Paruh Waktu"
                                elif pilihan == "3":
                                    kategori_dicari = "Profesional & Layanan Jasa"
                                else:
                                    print("Kategori tidak tersedia!")
                                    valid = False
                            elif pilihan != "1":
                                print("Pilihan tidak tersedia!")
                                valid = False
                                
                            if valid:
                                ditemukan = False
                                for key, job in adventures.items():
                                    if kategori_dicari == "" or job["kategori"] == kategori_dicari:
                                        print("-----------------------------------")
                                        print(f"ID         : {key}")
                                        print(f"Pekerjaan  : {job['nama']}")
                                        print(f"Kategori   : {job['kategori']}")
                                        print(f"Lokasi     : {job['lokasi']}")
                                        print(f"Kesulitan  : {job['kesulitan']}")
                                        print(f"Reward     : {job['reward']}")
                                        print(f"Status     : {job['status']}")
                                        ditemukan = True
                                if not ditemukan:
                                    print("Belum ada pekerjaan dalam kategori ini.")
                    
                    elif pilihan == "3":
                        print("\n========== UPDATE ADVENTURE ==========")

                        id_cari = input("Masukkan ID Adventure: ")

                        if id_cari in adventures:
                            job = adventures[id_cari]
                            print("Adventure ditemukan!")
                            print("Kosongkan nama atau lokasi jika tidak ingin mengubahnya.")

                            nama = input("Nama Baru: ")
                            if nama != "":
                                job["nama"] = nama

                            print("Ubah kategori? (y/n)")
                            ubah = input("Pilihan: ")

                            if ubah == "y":
                                print("\n1. Pekerjaan Utama (Buruh Harian)")
                                print("2. Pekerjaan Sampingan & Paruh Waktu")
                                print("3. Profesional & Layanan Jasa")
                            
                                pilihan_kategori = input("Pilih Kategori (1-3): ")

                                kategori = ""
                                if pilihan_kategori == "1":
                                    kategori = "Pekerjaan Utama (Buruh Harian)"
                                elif pilihan_kategori == "2":
                                    kategori = "Pekerjaan Sampingan & Paruh Waktu"
                                elif pilihan_kategori == "3":
                                    kategori = "Profesional & Layanan Jasa"

                                if kategori != "":
                                    job["kategori"] = kategori
                                else:
                                    print("Kategori tidak tersedia!")

                            lokasi = input("Lokasi Baru: ")
                            if lokasi != "":
                                job["lokasi"] = lokasi

                            print("Ubah kesulitan (y/n)")
                            if input("Pilihan: ") == "y":
                                kesulitan = input("Tingkat Kesulitan (1-5): ")

                                if kesulitan.isdigit():
                                    kesulitan = int(kesulitan)
                                    if 1 <= kesulitan <= 5:
                                        job["kesulitan"] = kesulitan
                                    else:
                                        print("Kesulitan tidak valid; nilai lama dipertahankan.")
                                else:
                                    print("Input harus berupa angka yang valid!")

                            print("Ubah reward (y/n)")
                            if input("Pilihan: ") == "y":
                                reward = input("Reward Baru: ")
                                if reward.isdigit():
                                    job["reward"] = int(reward)
                                else:
                                    print("Input harus berupa angka yang valid!")

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
                        else:
                            print("ID Adventure tidak ditemukan!")
                    
                    elif pilihan == "4":
                        print("\n========== DELETE ADVENTURE ==========")
                        id_cari = input("Masukkan ID Adventure: ")

                        if id_cari in adventures:
                            konfirmasi = input("Yakin Ingin Menghapus Pekerjaan Ini? (y/n): ")

                            if konfirmasi == "y":
                                del adventures[id_cari]
                                print("Adventure berhasil dihapus!")
                            else:
                                print("Penghapusan dibatalkan.")
                    
                    elif pilihan == "5":
                        print("Logout berhasil!")
                        break

                    
                    else:
                        print("\nPilihan tidak tersedia!")

            else:
                while True:
                    print("\n===== ADVENTURER MENU =====")
                    print("1. Lihat Adventure Board")
                    print("2. Logout")

                    pilihan = input("Pilih 1 Atau 2: ")

                    if pilihan == "1":
                        print("\n========== ADVENTURE BOARD ==========")

                        if len(adventures) == 0:
                            print("Belum ada pekerjaan.")
                        else:
                            print("1. Semua Pekerjaan")
                            print("2. Filter Berdasarkan Kategori")

                            pilihan = input("Pilih 1 Atau 2: ")

                            kategori_dicari = ""
                            valid = True

                            if pilihan == "2":
                                print("\n1. Pekerjaan Utama (Buruh Harian)")
                                print("2. Pekerjaan Sampingan & Paruh Waktu")
                                print("3. Profesional & Layanan Jasa")
                            
                                pilihan = input("Pilih Kategori (1-3): ")

                                if pilihan == "1":
                                    kategori_dicari = "Pekerjaan Utama (Buruh Harian)"
                                elif pilihan == "2":
                                    kategori_dicari = "Pekerjaan Sampingan & Paruh Waktu"
                                elif pilihan == "3":
                                    kategori_dicari = "Profesional & Layanan Jasa"
                                else:
                                    print("Kategori tidak tersedia!")
                                    valid = False

                            elif pilihan != "1":
                                print("Pilihan tidak tersedia!")
                                valid = False

                            if valid:
                                ditemukan = False

                                for key, job in adventures.items():
                                    if kategori_dicari == "" or job["kategori"] == kategori_dicari:
                                        print("-----------------------------------")
                                        print(f"ID         : {key}")
                                        print(f"Pekerjaan  : {job['nama']}")
                                        print(f"Kategori   : {job['kategori']}")
                                        print(f"Lokasi     : {job['lokasi']}")
                                        print(f"Kesulitan  : {job['kesulitan']}")
                                        print(f"Reward     : {job['reward']}")
                                        print(f"Status     : {job['status']}")

                                        ditemukan = True
                                if not ditemukan:
                                    print("Belum ada pekerjaan dalam kategori ini.")
                    
                    elif pilihan == "2":
                        print("Logout berhasil!")
                        break
                    
                    else:
                        print("\nPilihan tidak tersedia!")
        
        else:
            print("Username atau password salah!")

    elif pilihan == "2":
        print("\n========== REGISTER ==========")

        username = input("Buat Username: ")

        if username == "":
            print("Username tidak boleh kosong!")
        elif username in accounts:
            print("Username sudah digunakan!")
        else:
            password = input("Buat Password: ")

            if password == "":
                print("Password tidak boleh kosong!")
            else:
                accounts[username] = {"password": password, "role": "Pengguna"}
                print("Registrasi berhasil!")
            input("\nTekan Enter untuk melanjutkan...")

    elif pilihan == "3":
        print("See you on the next adventure!")
        break
    else:
        print("\nPilihan tidak tersedia!")

    input("\nTekan Enter untuk melanjutkan...")