'''
Wap to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the 
given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of 
both 3 and 5.
'''
n=int(input("enter a number : "))
if n%3==0 and n%5==0:
    print("Fizzbuzz")
elif n%5==0:
    print("buzz")
elif n%3==0:
    print("Fizz")
else:
    print("given number is not divisible by 3 as well as 5")
