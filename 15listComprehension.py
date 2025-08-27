# 🔢 Squaring Elements in a List
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original List:", lst)

# First squaring: [1, 4, 9, ..., 81]
lst = [i**2 for i in lst]
print("After First Squaring:", lst)

# Second squaring: [1, 16, 81, ..., 6561]
lst = [i**2 for i in lst]
print("After Second Squaring:", lst)
print('-' * 40)

# 🔍 Filtering Even Numbers
# Only include elements divisible by 2
print("Even Numbers:", [i for i in lst if i % 2 == 0])
print('-' * 40)

# 📊 Generating Multiplication Table Using List Comprehension
n = int(input("Enter a number: "))
print(f"Multiplication Table of {n}:", [i for i in range(n, n * 10 + 1, n)])
print('-' * 40)

# 🧮 Creating a Multi-Dimensional List (3x3 Matrix)
lst = [[j for j in range(1, 4)] for i in range(3)]
print("3x3 Matrix:", lst)
print('-' * 40)

# 🔍 Accessing Elements in Multi-Dimensional List

# Method 1: Reconstruct each row
print("Row-wise Access:", [[j for j in i] for i in lst])

# Method 2: Flatten the matrix
print("Flattened List (Method 1):", [j for i in lst for j in i])
print("Flattened List (Method 2):", [num for row in lst for num in row])