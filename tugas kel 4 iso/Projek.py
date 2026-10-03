opsi = 0

Nama_Anggota = ["Chika", "Rafa", "Rasyid", "Rheezam", "Mustafid", "Rifqi", "Daniel", "Alya", "Ridho", "Novi", "Rafie", "Rasya", "Nawfal", "Afuza", "Tri"]

while opsi != 7:
    print("Program Menampilkan data kelompok")
    print("1. Profil Kelompok")
    print("2. Nama Bindam")
    print("3. Lihat Nama Anggota Kelompok")
    print("4. Tambahkan Anggota Kelompok")
    print("5. Edit Nama Anggota")
    print("6. Hapus Anggota")
    print("7. Keluar")
    opsi = int(input("Pilih (1-7) : "))
   

    #Profil Kelompok
    if opsi == 1:
        print("Perkenalkan kami dari kelompok Cyber Security yang paling keren\n" \
              "dan kece abis. Makna dan Filosofi Logo kami adalah:")
        print("Lingkaran: Lingkaran melambangkan kesatuana, keamanan penuh, dan pengawasan tanpa celah")
        print("Terdapat 2 lingkaran yang bermakana lapisan keamanan ganda seperti firewall dan enkripsi")
        print("huruf c yang dibentuk dari setengah lingkaran yangb bisa dibaca sebagai simbol target atau radar")
        print("ada kunci mengunci data agar tidak bisa diakses sembarangan")
        print("warna biru: melambangkan profesional, dapat dipercaya, stabil. warna cyan/tosca yakni inovasi digital dan masa depan")
    elif opsi == 2:
        print("Muhammad Athaillah Cordova")
        print("Rafalia Khanza Taufik")
    elif opsi == 3:
        count = 0
        for nama in Nama_Anggota:
            print(str(count+1), ".", nama) 
            count += 1
    elif opsi == 4:
        NamaBaru = input("Masukkan nama anggota:")
        Nama_Anggota.append(NamaBaru)
    elif opsi == 5:
        print("")
    elif opsi == 6 :
        Pilihan = int(input("Pilih nomor anggota: "))
        Nama_Anggota.pop(Pilihan-1)
    else:
        print("JANGAN MASUKKAN ANGKA LAIN!")

print("Terima kasih sudah menggunnakan program")
#pilospi klmplk

#nama_Bindam =