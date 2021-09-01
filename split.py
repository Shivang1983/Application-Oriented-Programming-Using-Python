mystring=input("Enter the string:")
if " " in mystring:
    print("Entered string contains space so spilt() function will be executed :",list(mystring.split()))
else:
    print("Entered string does not contain any space in it") 