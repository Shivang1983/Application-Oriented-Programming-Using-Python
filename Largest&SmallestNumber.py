num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
numbers= [num1,num2,num3]
for lnum in numbers:
  if (num1 >= num2) and (num1 >= num3):
   lnum = num1
   break
  elif (num2 >= num1) and (num2 >= num3):
   lnum = num2
   break
  else:
   lnum = num3
   break
print("The largest number among",num1,",",num2,"and",num3,"is: ",lnum)
