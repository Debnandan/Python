# WAP to check the realtion between 2 integer number.
n1=int(input("enter number : "))
n2=int(input("enter number : "))
if n1>n2:
    print("n1 is greater")
elif n2>n1:
    print("n2 is greater")
elif n1<n2:
    print("n1 is smaller")
elif n2<n1:
    print("n2 is smaller")
else:
    print("both equal")
