'''
Consider a character input if it is uppercase convert it into lowercase, if it is lowercase
convert it into uppercase, if it is digit print the reminder when it is
divided by 3 else if it is special character print it’s ASCII value.

ch=input("enter a character : ")
if 'A'<=ch<='Z':
    print(ch.lower())
elif 'a'<=ch<='z':
    print(ch.upper())
elif '0'<=ch<='9':
    print(int(ch)%3)
else:
    print(ord(ch))
'''
ch=input("enter a character : ")
if 'A'<=ch<='Z':
    print(chr(ord(ch)+32))
elif 'a'<=ch<='z':
    print(chr(ord(ch)-32))
elif '0'<=ch<='9':
    print(int(ch)%3)
else:
    print(ord(ch))