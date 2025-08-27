# 🔁 Reverse a Number Using a While Loop

# Prompt user for input
num = int(input("Enter a number: "))

# Initialize the reversed number
rev = 0

# Loop until all digits are processed
while num > 0:
    digit = num % 10         # Extract the last digit
    rev = rev * 10 + digit   # Append digit to reversed number
    num = num // 10          # Remove the last digit from original number

# Display the result
print("Reverse of given number =", rev)