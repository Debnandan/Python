# 📋 Python List Operations

# 🔹 Creating a mixed-type list
lst = [1, 'Ashish', 21.5, True]
print("Original List:", lst)
print("-" * 15)

# 🔍 Accessing elements by index
print("Element at index 1:", lst[1])     # 'Ashish'
print("Last element:", lst[-1])          # True
print("-" * 15)

# ✏️ Modifying values
lst[2] = 'Rao'                           # Replace 21.5 with 'Rao'
print("Modified List:", lst)
print("-" * 15)

# ✂️ Slicing
print("Slice from index 1 to 2:", lst[1:3])  # ['Ashish', 'Rao']
print("-" * 15)

# 🔁 Reversing the list
print("Reversed List:", lst[::-1])
print("-" * 15)

# ➕ Appending an element
lst.append('hello')
print("After Appending:", lst)
print("-" * 15)

# ➖ Removing an element
lst.remove('hello')
print("After Removing 'hello':", lst)
print("-" * 15)

# 📏 Length of the list
print("Length of List:", len(lst))
print("-" * 15)

# 🔢 Sorting a numeric list
lst = [1, 5, 9, 4, 6, 3, 2, 8, 7]
print("Sorted List:", sorted(lst))       # Returns a new sorted list
print("-" * 15)

# 🔍 Finding index of an element
print("Index of 4:", lst.index(4))       # Returns index of first occurrence
print("-" * 15)

# 🔢 Counting occurrences
lst = [1, 2, 3, 2, 4, 2, 5, 6, 7, 2, 8]
print("Count of 2:", lst.count(2))       # Counts how many times 2 appears
print("-" * 15)

# 🔗 Extending the list
lst.extend(['hello', 'how', 'are', 'you'])
print("Extended List:", lst)
print("-" * 15)

# 📉 Finding min and max
lst = [1, 2, 3, 2, 4, 2, 5, 6, 7, 2, 8]
print("Minimum:", min(lst))
print("Maximum:", max(lst))
print("-" * 15)

# 🔁 Iterating over list (direct method)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Direct Iteration:")
for i in lst:
    print(i, end=" ")
print("\n" + "-" * 15)

# 🔁 Iterating using index (indirect method)
print("Indirect Iteration:")
for i in range(len(lst)):
    print(lst[i], end=" ")
print("\n" + "-" * 15)

# 🔁 Iterating in reverse
print("Reverse Iteration:")
for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end=" ")