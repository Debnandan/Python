# 🧠 Python Dictionary Operations

# 🔹 Initializing a dictionary
a = {1: 'Ashish', 2: 'Nehra'}
print("Initial Dictionary:", a)

# 🔹 Duplicate keys: last value overwrites previous
a = {1: 'Ashish', 1: 'Nehra'}  # Key 1 appears twice; 'Nehra' overwrites 'Ashish'
print("After Duplicate Key Assignment:", a)
print('- -' * 20)

# 🔍 Accessing dictionary elements
dct = {1: 'Ashish', 2: 'Avneet', 3: 'Riya', 4: 'Ankur', 5: 'Sakshi'}
print("Full Dictionary:", dct)
print("Access with [1]:", dct[1])         # Direct access
print("Access with get(1):", dct.get(1))  # Safe access
print('- -' * 20)

# ✏️ Adding, Updating, and Deleting Key-Value Pairs
print("Before Modification:", dct)
dct[6] = 'Rahul'         # Add new key
print("After Adding Key 6:", dct)
dct[6] = 'Ankita'        # Update key 6
print("After Updating Key 6:", dct)
del dct[6]               # Delete key 6
print("After Deleting Key 6:", dct)
print('- -' * 20)

# 🧹 Clearing the Dictionary
print("Before Clearing:", dct)
dct.clear()              # Removes all items
print("After Clearing:", dct)
print('- -' * 20)

# 🔁 Iterating Through Dictionary
dct = {1: 'Ashish', 2: 'Avneet', 3: 'Riya', 4: 'Ankur', 5: 'Sakshi'}
print("Keys:", dct.keys())       # Returns all keys
print("Values:", dct.values())   # Returns all values
print('- -' * 20)

# 🔄 Looping Through Keys
print("Looping through keys:")
for k in dct.keys():
    print(k, dct[k])

# 🔄 Looping Through Items (key-value pairs)
print("Items:", dct.items())
print("Looping through items:")
for k, v in dct.items():
    print(k, v)
print('- -' * 20)