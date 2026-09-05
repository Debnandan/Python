# Wap to print the middle value of a list only if it is string.
l=eval(input("enter a list : "))
if len(l)%2!=0:
    if type(l[len(l)//2])==str:
        print(l[len(l)//2])
    else:
        print("middle value containing another datatype")
else:
    print("list does not having middle value")