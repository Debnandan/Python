# WAP to check whether 2 values are pointing towards to same memory or not.
data1=eval(input("enter the first value : "))
data2=eval(input("enter the second value : "))
if data1 is data2:
    print("same address")
else:
    print("different address")