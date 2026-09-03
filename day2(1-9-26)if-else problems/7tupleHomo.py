# Considera tuple of length 2 and check whether the tuple is homogeneous.
t=eval(input("enter the tuple : "))
if len(t) == 2 and type(t[0])==type(t[1]):
    print("homogeneous")
else:
    print("heterogeneous or len is not 2")