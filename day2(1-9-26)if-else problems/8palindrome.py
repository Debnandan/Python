# WAP to check whether the given string is palindrome.
s=input("enter the str : ")
if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")