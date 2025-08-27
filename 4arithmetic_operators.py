# Arithmetic Operations in Python

# ➕ Addition
print("Addition -------------------")
print(2 + 3)               # Integer + Integer
print(2.5 + 3.5)           # Float + Float
print(2 + 3.5)             # Integer + Float
print("hello " + "buddy") # String concatenation
print(True + True)        # Boolean addition: True = 1, so 1 + 1 = 2

# ➖ Subtraction
print("\nSubtraction -------------------")
print(2 - 3)               # Integer - Integer
print(3.5 - 2.5)           # Float - Float
print(2 - 1.3)             # Integer - Float
print(False - True)       # Boolean subtraction: False = 0, True = 1 → 0 - 1 = -1

# ✖️ Multiplication
print("\nMultiplication -------------------")
print(2 * 3)               # Integer * Integer
print(3.5 * 2.5)           # Float * Float
print(2 * 1.3)             # Integer * Float
print(False * True)       # Boolean multiplication: 0 * 1 = 0

# ➗ Division
print("\nDivision -------------------")
print(5 / 2)               # Regular division returns float
print(3.5 / 2.5)
print(2 / 1.3)

# 🔢 Floor Division
print("\nFloor Division -------------------")
# Returns the integer part of the quotient (rounded down)
print(5 // 2)
print(3.5 // 2.5)
print(2 // 1.3)

# 🧮 Modulo
print("\nModulo -------------------")
# Returns the remainder of division
print(5 % 2)
print(3.5 % 2.5)
print(2 % 1.3)

# 🧠 Exponentiation
print("\nExponentiation -------------------")
# Raises the first number to the power of the second
print(5 ** 2)
print(3.5 ** 2.5)
print(2 ** 1.3)

# 📌 Absolute Value
print("\nAbsolute Value -------------------")
# Converts negative numbers to positive
print(abs(-43))
print(abs(-4.5))

# 🔁 Rounding
print("\nRounding -------------------")
# Rounds a float to the specified number of decimal places
print(round(1.23456789, 3))

# ⚡ Power Function
print("\nPower Function -------------------")
# Equivalent to exponentiation: pow(base, exponent)
print(pow(5, 6))