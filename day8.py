#Develop a Python program to concatenate two lists into a single list, adhering to the following requirements:
# 1. Define two distinct lists.
# 2. Design a function that accepts both lists as parameters and return a new list comprising elements from both input lists.
# 3. Print the resulting concatenated list.

def concatenate_lists(list1,list2):
 return list1+list2
a=[1,2,3]
b=['a','b','c']
list3=concatenate_lists(a,b) 
print(list3)
