
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
Prodi=input("Program Studi: ")
resolusi = input("Masukkan Resolusi di Tahun ini: ")



with open("Me.txt", "w") as file:
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Resolusi Tahun Ini: {resolusi}\n")
    file.write(f"Program Studi: {Prodi}\n")


print("File Me.txt telah berhasil dibuat!")
