# WAP to print cube of a number only if it is divisible by 9 or 6.
n=int(input('enter a number : '))
if n%9==0 or n%6==0:
    print(n**3)