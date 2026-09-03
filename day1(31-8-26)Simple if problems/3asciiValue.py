# WAP to print ASCII value of a character only if its in Uppercase.
char=input('enter a char : ')
if 'A' <= char <= 'Z':
    print(ord(char))