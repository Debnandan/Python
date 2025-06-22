# concatenation
print("hello","world")
print("-"*20)

# replication
print("hello "*5)
print("-"*20)

# length
print(len("hello "))
print("-"*20)

# slicing
print("hello world"[4])
print("hello world"[-1])
print("hello world"[:5])
print("hello world"[::-1])  # reverse
print("-"*20)


# case conversion
print("hello world".upper())
print("hello WORLD".lower())
print("-"*20)

# stripping
print("      hello       ".strip())
print("-"*20)

# replacing
print("potato".replace('o','*'))
print("-"*20)

# count
print("DebnandaN".count('n'))
print("DebnandaN".count('N'))
print("DebnandaN".lower().count('n')) # to count total number of n present in the string
print("-"*20)

# check
print("hello".isalpha())
print("1234".isdigit())
print("hello".islower())
print("HELLO".isupper())
print("-"*20)

# capitalisation
print("hello world".capitalize())
print("hello world".title())
print("-"*20)

# check for start and end
print("hello world".startswith("hel"))
print("hello world".endswith("ld"))
print("-"*20)

# making a string to the fixed length
print("hello world".center(20,"*"))
print("hello world".ljust(20,"*"))
print("hello world".rjust(20,"*"))