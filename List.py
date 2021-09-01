# List in Python example - Code & Output
list=[1,2,3,'study',123]
print(list[-1]) #It will display last element
print(list[3:]) #All the element starting from 3 upto end will be displaying
print(list[:4]) #All elements will be displayed upto index 4.
print(list[0:6]) #All the elements will be displayed
# Question 1 Code & Output
list=[1,2,2.2,2,1,"Python"]
#Length of list
n=len(list)
print(n)
# To check if 2.2 element in list using for loop
list=[1,2,2.2,2,1,"Python"]
for i in list:
    list_count=list.count(2.2)
    if list_count>0:
        print("Element is present:",2.2)
        break
    else:
        print("Element is not present:",2.2)
#Use of sort() with an example
# sort() is used to sort the list ascending by default
vowels=['e','a','i','o','u']
print("Vowels before sort():",vowels)
vowels.sort()
print("Vowels after sort():",vowels) 