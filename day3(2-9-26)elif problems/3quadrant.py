x=int(input("enter x :"))
y=int(input("enter y :"))
if x>=0 and y>=0:
    print("1st quadrant")
elif x>=0 and y<0:
    print("4 quadrant")
elif x<0 and y>=0:
    print("2 quadrant")
else:
    print("3 quadrant")
