import random

word_list = ["komputer", "program", "python", "hangman", "universitas", "mahasiswa", "algoritma"]

hangman_pics = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_"] * word_length


lives = len(hangman_pics) - 1
guessed_letters = []

print("Selamat datang di Hangman!\n")


while lives > 0 and "_" in display:
    print(hangman_pics[len(hangman_pics) - 1 - lives])
    print("Kata:", " ".join(display))
    print(f"Sisa nyawa: {lives}")
    guess = input("Tebak sebuah huruf: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Masukkan hanya satu huruf!\n")
        continue

    if guess in guessed_letters:
        print(f"Kamu sudah menebak huruf '{guess}'. Coba huruf lain.\n")
        continue
    else:
        guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Tebakanmu benar!\n")
    else:
        lives -= 1
        print(f"Salah! Huruf '{guess}' tidak ada dalam kata.\n")

# Hasil akhir
if "_" not in display:
    print(f"Selamat! Kamu berhasil menebak kata: {chosen_word}")
else:
    print(hangman_pics[-1])
    print(f"Game over! Kata yang benar adalah: {chosen_word}")

