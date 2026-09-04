'''
WAP to check whether the given integer is single digit, double digit, triple digit 
or more than that.
'''
n=abs(int(input("enter a number : ")))
m=str(n)
if len(m)==1:
    print("single digit")
elif len(m)==2:
    print("double digit")
elif len(m)==3:
    print("triple digit")
else:
    print("more digit")

