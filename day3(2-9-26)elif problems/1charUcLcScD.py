# WAP to check Whether the char is Uppercase, Lowercase, Digit and Special Character.
s=input("enter a character : ")
if 'A'<=s<='Z':
    print("uppercase")
elif 'a'<=s<='z':
    print("lowercase")
elif '0'<=s<='9':
    print("digit")
else:
    print("special case")
