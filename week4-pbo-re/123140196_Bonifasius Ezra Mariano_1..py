import random

baris, kolom = 3, 3

papan = [['?' for _ in range(kolom)] for _ in range(baris)]

posisi_bom_baris = random.randint(0, baris - 1)
posisi_bom_kolom = random.randint(0, kolom - 1)

def cetak_papan():
    for baris_papan in papan:
        print(' '.join(baris_papan))
    print()

jumlah_kotak_terbuka = 0
jumlah_kotak_harus_dibuka = baris * kolom - 1  

print("=== Selamat datang di permainan Minesweeper 3x3! ===")
cetak_papan()

while True:
    try:
        input_baris = int(input("Pilih baris (1-3): ")) - 1
        input_kolom = int(input("Pilih kolom (1-3): ")) - 1
    except ValueError:
        print("Masukkan angka yang benar!")
        continue

    if not (0 <= input_baris < baris and 0 <= input_kolom < kolom):
        print("Pilihan di luar batas papan! Silakan coba lagi.")
        continue

    if papan[input_baris][input_kolom] != '?':
        print("Kotak ini sudah dibuka. Pilih kotak lain!")
        continue

    if input_baris == posisi_bom_baris and input_kolom == posisi_bom_kolom:
        papan[input_baris][input_kolom] = 'X'
        cetak_papan()
        print("Boom! Kamu menginjak bom. Game over!")
        break
    else:
        papan[input_baris][input_kolom] = 'O'
        jumlah_kotak_terbuka += 1
        cetak_papan()

    if jumlah_kotak_terbuka == jumlah_kotak_harus_dibuka:
        print("Selamat! Kamu telah membuka semua kotak dan menang!")
        break
