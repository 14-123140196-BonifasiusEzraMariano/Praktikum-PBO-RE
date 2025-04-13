def tampilkan_menu():
    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tambah_tugas(daftar):
    try:
        tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
        if not tugas:
            raise ValueError("Tugas tidak boleh kosong.")
        daftar.append(tugas)
        print("Tugas berhasil ditambahkan!")
    except ValueError as e:
        print(f"Error: {e}")

def hapus_tugas(daftar):
    try:
        if not daftar:
            raise IndexError("Daftar tugas kosong. Tidak ada yang bisa dihapus.")
        
        for idx, tugas in enumerate(daftar, 1):
            print(f"{idx}. {tugas}")
        
        nomor = input("Masukkan nomor tugas yang ingin dihapus: ")
        if not nomor.isdigit():
            raise ValueError("Harap masukkan nomor yang valid.")
        
        nomor = int(nomor)
        if nomor < 1 or nomor > len(daftar):
            raise IndexError(f"Tugas dengan nomor {nomor} tidak ditemukan.")
        
        tugas_dihapus = daftar.pop(nomor - 1)
        print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

def tampilkan_daftar(daftar):
    if not daftar:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for tugas in daftar:
            print(f"- {tugas}")

def main():
    daftar_tugas = []

    while True:
        try:
            tampilkan_menu()
            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
            
            if pilihan == "1":
                tambah_tugas(daftar_tugas)
            elif pilihan == "2":
                hapus_tugas(daftar_tugas)
            elif pilihan == "3":
                tampilkan_daftar(daftar_tugas)
            elif pilihan == "4":
                print("Keluar dari program.")
                break
            else:
                raise ValueError("Pilihan tidak valid. Harap masukkan 1, 2, 3, atau 4.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
