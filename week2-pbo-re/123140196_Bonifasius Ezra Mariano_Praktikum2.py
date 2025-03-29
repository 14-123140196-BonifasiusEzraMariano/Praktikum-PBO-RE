import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Child:
    def __init__(self, father, mother):
        self.father_alleles = list(father.blood_type)  # Pisahkan alel ayah
        self.mother_alleles = list(mother.blood_type)  # Pisahkan alel ibu
        
        inherited_alleles = random.choice(self.father_alleles) + random.choice(self.mother_alleles)

        self.blood_type = self.determine_blood_type(inherited_alleles)

    def determine_blood_type(self, alleles):
        if "A" in alleles and "B" in alleles:
            return "AB"
        elif "A" in alleles:
            return "A"
        elif "B" in alleles:
            return "B"
        else:
            return "O"

def get_valid_blood_type(prompt):
    valid_blood_types = ["A", "B", "AB", "O"]
    while True:
        blood_type = input(prompt).strip().upper()
        if blood_type in valid_blood_types:
            return blood_type
        print("⚠ Golongan darah tidak valid! Masukkan hanya A, B, AB, atau O.")

father_blood = get_valid_blood_type("Masukkan golongan darah ayah (A, B, AB, O): ")
mother_blood = get_valid_blood_type("Masukkan golongan darah ibu (A, B, AB, O): ")

father = Father(father_blood)
mother = Mother(mother_blood)

child = Child(father, mother)

print(f"Golongan darah anak: {child.blood_type}")
