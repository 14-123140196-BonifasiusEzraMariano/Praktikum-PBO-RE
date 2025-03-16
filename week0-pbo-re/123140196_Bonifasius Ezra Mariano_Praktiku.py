tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(0,tinggi+1):
    print(" " * (tinggi - i) + "*" * (2 * i - 1) )

    
