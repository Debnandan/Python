'''
1-> consider a dictionary consist of username as key and values as password 
    check if the entered username and password is valid or not.
'''
d={'debnandan':1234,'rahul':'kumar','chacha':'cutie','rinky':'kuch bhi'}
un = input("enter username : ")
if un in d:
    pwd = eval(input("enter password : "))
    if pwd == d[un]:
        print("login")
    else:
        print("invalid passowrd")
else:
    print("user not found")