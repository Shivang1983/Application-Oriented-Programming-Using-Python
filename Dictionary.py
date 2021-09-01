#Finding Length of my_dict
my_dict={'name':'Ram', 'rollno':11}
c=len(my_dict)
print("Length of my_dict is :",c)
#insert two new keys and values
my_dict["marks"]=[100,101]
my_dict['subject']=['c','java']
print("After adding two keys and values :",my_dict)
#checking if subj key is present in python
print("Checking if subj key is present in Dictionary:")
if 'subj' in my_dict:
    print("subj Key is present in Dictionary")
else:
    print("subj Key is not present in Dictionary")
# Copying this dictionary to backup_dictionary
backup_dictionary=my_dict.copy()
#deleting key rollno
my_dict.pop('rollno')
print("dictionary after removal of roll no key in my_dict is:",my_dict)
#using clear()
my_dict.clear()
print("After using clear() function in my_dict:",my_dict)
#now performing all operations with backup_dictionary
backup_dictionary.pop('rollno')
print("dictionary after removal of roll no key in backup_dictionary is:",backup_dictionary)
#clear backup dictionary
backup_dictionary.clear()
print("After using clear() function in backup_dictionary:",backup_dictionary)
#using zip() method to update keys and values in backup_dictionary
l1=["university","branch","city","contactno"]
l2=["gu","mca","Noida","33333"]
backup_dictionary=dict(zip(l1, l2))
print("After updating backup_dictionary using zip()",backup_dictionary)
#printing all keys & values using items()
print("backup_dictionary items in tuple form:",backup_dictionary.items())