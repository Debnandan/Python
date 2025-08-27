# 🔍 Comparison Operators in Python

# ✅ Equality (==)
print("Equality (==) ------------------------")
print(1 == 2)             # False: 1 is not equal to 2
print(1.0 == 1)           # True: float and int with same value are equal
print(False == True)      # False: Boolean values differ
print(True == 1)          # True: True is treated as 1
print(False == 0)         # True: False is treated as 0
print('A' == "A")         # True: single and double quotes are equivalent
print('A' == "a")         # False: case-sensitive comparison

# ❌ Inequality (!=)
print("\nInequality (!=) ------------------------")
print(1 != 2)             # True: 1 is not equal to 2
print(1.0 != 1)           # False: values are equal
print(False != True)      # True: Boolean values differ
print(True != 1)          # False: True is treated as 1
print(False != 0)         # False: False is treated as 0
print('A' != "A")         # False: same character
print('A' != "a")         # True: case-sensitive comparison

# 🔽 Less Than (<)
print("\nLess Than (<) ------------------------")
print(1 < 2)              # True: 1 is less than 2

# 🔼 Greater Than (>)
print("\nGreater Than (>) ------------------------")
print(2 > 1)              # True: 2 is greater than 1

# 🔁 Less Than or Equal (<=)
print("\nLess Than or Equal (<=) ------------------------")
print(1 <= 2)             # True: 1 is less than 2
print(2 <= 2)             # True: 2 is equal to 2

# 🔁 Greater Than or Equal (>=)
print("\nGreater Than or Equal (>=) ------------------------")
print(1 >= 2)             # False: 1 is not greater than or equal to 2
print(2 >= 2)             # True: 2 is equal to 2