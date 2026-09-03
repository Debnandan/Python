# WAP to check whether the data is mutable or not.
data = eval(input("enter the data : "))
if type(data) in [list,set,dict]:
    print("data is mutable")
else:
    print("data is im-mutable")
