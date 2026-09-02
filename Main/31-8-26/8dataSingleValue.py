# WAP to check the given data is of single value data type.
data = eval(input("enter the data : "))
if type(data) == int or type(data) == float or type(data) == bool or type(data) == complex:
    print("data is single value data type")