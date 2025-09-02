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
print('- -' * 20) 

# 🔄 Looping Through Items (key-value pairs)
print("Items:", dct.items())
print("Looping through items:")
for k, v in dct.items():          # key,value
    print(k, v)
print('- -' * 20) 

# 🔍 Key Presence
print(dct)
print(1 in dct)     # True: integer key exists
print('1' in dct)   # False: string key doesn't
print('- -' * 20) 

# 🔄 Update with Another Dictionary

# Original dictionaries
dct1 = {1: 'a', 2: 'b', 3: 'c', 5: 'e'}
dct2 = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
dct1.update(dct2)               # Update dct1 with dct2
print("Updated dct1:", dct1)    # ✅ Result: matching keys are overwritten, new keys are added
                                # Output: {1: 'A', 2: 'B', 3: 'C', 5: 'e', 4: 'D'}