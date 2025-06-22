num=int(input("enter a number : "))
rem=0
while(num>0):
    rem += num%10
    rem *= 10
    num = num//10
print("reverse of given number =",num)
