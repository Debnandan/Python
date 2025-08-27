# 🔄 Type Conversion in Python

# 🧮 int() Conversion
print("int Conversion ------------------")
print(3.14)                  # Original float value
print(int(3.14))             # Converts float to int (truncates decimal)
print(int(' 10 '))           # Converts string with spaces to int
# Note: '10 5' would raise an error because it's not a valid single number
print(int(True))             # True → 1
print(int(False))            # False → 0

# 🌊 float() Conversion
print("\nfloat Conversion ------------------")
print(float(6))              # Integer to float
print(float(True))           # True → 1.0
print(float("10"))           # String to float
print(float("10.5"))         # String with decimal to float

# 📝 str() Conversion
print("\nstr Conversion ------------------")
print(str(10))               # Integer to string
print(str(10.7))             # Float to string
print(str(True))             # Boolean to string

# ✅ bool() Conversion
print("\nbool Conversion ------------------")
print(bool(10))              # Non-zero → True
print(bool(10.5555))         # Non-zero float → True
print(bool(0))               # Zero → False
print(bool(""))              # Empty string → False
print(bool(" "))             # String with space → True
print(bool("1665161"))       # Non-empty string → True

# 🔁 Convert "3.14" (string) to int
print("\nConvert '3.14' string to int ------------------")
print(int(float("3.14")))    # First convert to float, then to int