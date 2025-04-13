from abc import ABC, abstractmethod

# Kelas Abstrak
class Animal(ABC):
    def __init__(self, name, age):
        if not name.strip():
            raise ValueError("Nama hewan tidak boleh kosong.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Usia hewan harus berupa angka positif.")

        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not new_name.strip():
            raise ValueError("Nama baru tidak boleh kosong.")
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if not isinstance(new_age, int) or new_age <= 0:
            raise ValueError("Usia harus berupa angka positif.")
        self.__age = new_age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def deskripsi(self):
        pass


# Subclass untuk setiap hewan
class Dog(Animal):
    def make_sound(self):
        return "Guk guk!"
    
    def deskripsi(self):
        return "Hewan bertipe karnivora yang suka menggonggong keras"

class Cat(Animal):
    def make_sound(self):
        return "Meong~"

    def deskripsi(self):
        return "Hewan kecil yang lincah dan suka tidur di tempat hangat pemakan daging"

class Lion(Animal):
    def make_sound(self):
        return "Raawrr!"

    def deskripsi(self):
        return "Singa adalah raja hutan yang memiliki auman menggelegar yang suka memangsa hewan herbivora"

class Elephant(Animal):
    def make_sound(self):
        return "Bruummm!"

    def deskripsi(self):
        return "Gajah adalah hewan darat terbesar dengan belalai panjang yang suka memakan buah,daun dan rumput"

class Bird(Animal):
    def make_sound(self):
        return "Cuit cuit!"

    def deskripsi(self):
        return "Burung adalah hewan bersayap yang bisa terbang dan berkicau suka memakan biji-bijian"

class Tiger(Animal):
    def make_sound(self):
        return "Grrrhh!"

    def deskripsi(self):
        return "Harimau adalah predator kuat dengan garis-garis hitam khas yang suka memangsa hewan herbivora"

class Monkey(Animal):
    def make_sound(self):
        return "Oo oo aa aa!"

    def deskripsi(self):
        return "Kera adalah hewan cerdas dan aktif yang suka memanjat dan suka memakan buah-buahan"


# Fungsi tampilan
def tampilkan_hewan(zoo):
    if not zoo:
        print("Belum ada hewan yang terlindungi.")
    else:
        print("\nDaftar Hewan yang Dilindungi:")
        for idx, animal in enumerate(zoo, 1):
            print(f"{idx}. {animal.get_name()} ({animal.__class__.__name__}, {animal.get_age()} tahun)")
            print(f"   Suara     : {animal.make_sound()}")
            print(f"   Deskripsi : {animal.deskripsi()}")


# Main Program
def main():
    zoo = []

    while True:
        try:
            print("\n=== Sistem Perlindungan Hewan ===")
            print("1. Tambah hewan")
            print("2. Tampilkan semua hewan")
            print("3. Keluar")
            pilihan = input("Masukkan pilihan (1/2/3): ")

            if pilihan == "1":
                print("\nPilih jenis hewan:")
                print("1. Anjing")
                print("2. Kucing")
                print("3. Singa")
                print("4. Gajah")
                print("5. Burung")
                print("6. Harimau")
                print("7. Kera")
                jenis = input("Pilihan jenis (1-7): ")

                nama = input("Masukkan nama hewan: ")
                usia_input = input("Masukkan usia hewan: ")
                if not usia_input.isdigit():
                    raise ValueError("Usia harus berupa angka.")

                usia = int(usia_input)

                jenis_dict = {
                    "1": Dog,
                    "2": Cat,
                    "3": Lion,
                    "4": Elephant,
                    "5": Bird,
                    "6": Tiger,
                    "7": Monkey
                }

                if jenis not in jenis_dict:
                    raise ValueError("Pilihan jenis hewan tidak valid.")

                hewan = jenis_dict[jenis](nama, usia)
                zoo.append(hewan)
                print("Hewan berhasil ditambahkan ke daftar perlindungan!")

            elif pilihan == "2":
                tampilkan_hewan(zoo)

            elif pilihan == "3":
                print("Keluar dari program Perlindungan Hewan.")
                break

            else:
                raise ValueError("Pilihan menu tidak valid. Harap masukkan 1, 2, atau 3.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
