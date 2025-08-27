# 🧮 Working with Nested Lists (2D Lists)

# 🔹 Initial 2D list
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original List:")
print(lst)
print("-" * 40)

# 🔍 Accessing elements
print("First row:", lst[0])         # Access entire first sublist
print("Second element of first row:", lst[0][1])  # Access specific element
print("-" * 40)

# ✏️ Modifying values
print("Before Modification:", lst)
lst[0][1] = 7                       # Change 2 to 7 in first row
lst[1] = [6, 5, 4]                  # Replace entire second row
print("After Modification:", lst)
print("-" * 40)

# ✂️ Slicing rows
print("Sliced rows (0 to 1):", lst[0:2])  # First two rows
print("-" * 40)

# ➕ Appending a new row
lst.append([10, 11, 12])
print("After Appending:", lst)
print("-" * 40)

# ➖ Removing a row
del lst[0]                          # Delete first row
print("After Deletion:", lst)
print("-" * 40)

# 📏 Length of outer list (number of rows)
print("Number of rows:", len(lst))
print("-" * 40)

# 🔁 Reversing the outer list
print("Reversed List:", lst[::-1])
print("-" * 40)

# 🔍 Accessing all rows
print("Each row:")
for row in lst:
    print(row)

# 🔍 Accessing all elements
print("All elements:")
for row in lst:
    for element in row:
        print(element)