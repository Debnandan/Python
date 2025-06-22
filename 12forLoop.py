# printing table
n=int(input("enter a number : "))
for i in range(n,(n*10)+1,n):
    print(i,end=(" "))
print("-"*15)

# finding probability of getting numbers 1 to 12 by summation of rolling 2 dices
for j in range(1,13):
    number=0
    for k in range(1,7):
        for m  in range(1,7):
            if(k+m==j):
                number += 1
    print("probability of getting",j,"=",round(number/0.36,2))
print("-"*15)

# You are given a String S, you need to print its characters at even indices(index starts at 0).
s = "Geeks"
for a in range(0, len(s), 2):  # Start at 0, step by 2
    print(s[a], end='')
    