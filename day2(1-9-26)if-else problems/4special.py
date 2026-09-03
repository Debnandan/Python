# WAP to check whether the given char is special or not.
data = input("enter a character :")
if not('a'<=data<='z' or 'A'<=data<='Z' or '0'<=data<='9'):
    print("entered data is special")
else:
    print("entered data is not special")
            
