# 🧠 Different Ways to Assign Values to Variables

# 🔹 Single assignments
a = 1
b = 2

# 🔹 Multiple variables assigned the same value
c = d = e = 3

# 🔹 Multiple assignments with different values
f, g, h = 4, 5, 6

# ✅ Print all assigned values
print("Single & Multiple Assignments:")
print(a, b, c, d, e, f, g, h)

# 🔹 Unpacking a list into variables
data = [7, 8, 9]
i, j, k = data

print("\nUnpacking List:")
print(i, j, k)

# 🔹 Input and type conversion
n = int(input("\nEnter a number: "))  # Converts user input to integer
print("You entered:", n)

# 🔹 Arithmetic operation with assignment
n += 1  # Equivalent to: n = n + 1  
print("After incrementing by 1:", n)