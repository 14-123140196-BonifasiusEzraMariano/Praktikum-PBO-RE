import math

while True:
    try:
        user_input = input("Masukkan angka: ")
        angka = float(user_input)

        if angka < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
        elif angka == 0:
            print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
        else:
            akar = math.sqrt(angka)
            print(f"Akar kuadrat dari {angka} adalah {akar}")
            break  # Keluar dari loop setelah input valid dan hasil ditampilkan

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")
