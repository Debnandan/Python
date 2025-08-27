# 🔍 Check if a number is positive, negative, or zero

# Prompt user for input and convert it to an integer
num = int(input("Enter a number: "))

# 🧠 Conditional logic
if num > 0:
    print(num, "is positive")   # Executes if number is greater than 0
elif num < 0:
    print(num, "is negative")   # Executes if number is less than 0
else:
    print(num, "is zero")       # Executes if number is exactly 0