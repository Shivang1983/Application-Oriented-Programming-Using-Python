a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))       

def maxinthree(a,b,c):
    if a>b:
        if a>c:
            return(a)
        else:
            return(c)
    elif b>c:
        return(b)
    else: 
        return(c)

print(maxinthree(a,b,c))