# 📊 Printing Multiplication Table of a Number
n = int(input("Enter a number: "))
for i in range(n, (n * 10) + 1, n):
    print(i, end=" ")
print("\n" + "-" * 15)

# 🎲 Probability of Getting Sums from 2 Dice Rolls
# Total outcomes when rolling two dice = 6 * 6 = 36
# Probability of a sum = (favorable outcomes) / 36
# To express as percentage, divide by 0.36 (i.e., 36/100)
for j in range(1, 13):  # Possible sums range from 2 to 12
    count = 0
    for k in range(1, 7):      # First die
        for m in range(1, 7):  # Second die
            if k + m == j:
                count += 1
    probability = round(count / 0.36, 2)  # Convert to percentage
    print(f"Probability of getting {j} = {probability}%")
print("-" * 15)

# 🔡 Print Characters at Even Indices of a String
s = "Geeks"
print("Characters at even indices:")
for a in range(0, len(s), 2):  # Start at 0, step by 2
    print(s[a], end='')