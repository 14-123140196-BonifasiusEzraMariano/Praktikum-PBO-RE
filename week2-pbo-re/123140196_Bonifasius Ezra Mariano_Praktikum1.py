import math

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Division by zero is not allowed")
        return Calculator(self.value / other.value)

    def __pow__(self, other):
        return Calculator(self.value ** other.value)
    
    def __mod__(self, other):
        if self.value <= 0 or other.value <= 0:
            raise ValueError("Logarithm is undefined for non-positive values")
        return Calculator(math.log(self.value, other.value))

    def __repr__(self):
        return f"Calculator({self.value})"

# Contoh penggunaan
x = Calculator(2)
y = Calculator(8)

print(x + y)  # Penjumlahan
print(x - y)  # Pengurangan
print(x * y)  # Perkalian
print(x / y)  # Pembagian
print(x ** y) # Pangkat
print(x % y)  # Logaritma x log y
