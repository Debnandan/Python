# WAP to check smallest of 3 numbers.
n1=int(input("enter number : "))
n2=int(input("enter number : "))
n3=int(input("enter number : "))
if n1<n2 and n1<n3:
    print("first number smaller")
elif n2<n3:
    print("second number smaller")
else:
    print("third number smaller")
