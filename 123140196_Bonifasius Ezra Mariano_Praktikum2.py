data = {}

mahasiswa=int(input(" masukkan jumlah mahasiswa "))


for i in range(mahasiswa):
    nama = input(f"Masukkan nama ke-{i+1}: ")
    nilai = input(f"Masukkan nilai untuk {nama}: ")
    data[nama] = nilai


print(f"dictionary ={data} ")
