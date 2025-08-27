# 🧵 String Operations in Python

# 🔗 Concatenation
print("Concatenation ------------------")
print("hello", "world")         # Prints with space between
print("-" * 20)

# 🔁 Replication
print("Replication ------------------")
print("hello " * 5)             # Repeats the string 5 times
print("-" * 20)

# 📏 Length
print("Length ------------------")
print(len("hello "))            # Counts characters including space
print("-" * 20)

# ✂️ Slicing
print("Slicing ------------------")
print("hello world"[4])         # Character at index 4 → 'o'
print("hello world"[-1])        # Last character → 'd'
print("hello world"[:5])        # First 5 characters → 'hello'
print("hello world"[::-1])      # Reversed string
print("-" * 20)

# 🔠 Case Conversion
print("Case Conversion ------------------")
print("hello world".upper())    # All uppercase
print("hello WORLD".lower())    # All lowercase
print("-" * 20)

# 🧼 Stripping Whitespace
print("Stripping ------------------")
print("      hello       ".strip())  # Removes leading/trailing spaces
print("-" * 20)

# 🔄 Replacing Characters
print("Replacing ------------------")
print("potato".replace('o', '*'))    # Replaces all 'o' with '*'
print("-" * 20)

# 🔢 Counting Characters
print("Counting ------------------")
print("DebnandaN".count('n'))        # Counts lowercase 'n'
print("DebnandaN".count('N'))        # Counts uppercase 'N'
print("DebnandaN".lower().count('n'))# Counts all 'n' after lowering case
print("-" * 20)

# ✅ String Checks
print("Checks ------------------")
print("hello".isalpha())        # True: all alphabetic
print("1234".isdigit())         # True: all digits
print("hello".islower())        # True: all lowercase
print("HELLO".isupper())        # True: all uppercase
print("-" * 20)

# 🧢 Capitalization
print("Capitalization ------------------")
print("hello world".capitalize())    # First letter capitalized
print("hello world".title())         # Each word capitalized
print("-" * 20)

# 🔍 Start/End Checks
print("Start/End Checks ------------------")
print("hello world".startswith("hel"))  # True
print("hello world".endswith("ld"))     # True
print("-" * 20)

# 📐 Fixed-Length Formatting
print("Fixed-Length Formatting ------------------")
print("hello world".center(20, "*"))    # Centered with '*'
print("hello world".ljust(20, "*"))     # Left-justified with '*'
print("hello world".rjust(20, "*"))     # Right-justified with '*'

#    ****hello world*****
#    hello world*********
#    *********hello world 