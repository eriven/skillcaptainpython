'''Compose a Python program to execute various operations on a given dictionary:
1. Insert a new key-value pair into the dictionary.  2. Delete a designated key-value pair from the dictionary.  3. Modify the value associated with a specified key in the dictionary.  4. Verify the existence of a key in the dictionary.  5. Display all the keys present in the dictionary.
Output:
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
{'a': 1, 'c': 3, 'd': 4}
{'a': 10, 'c': 3, 'd': 4}
True
['a', 'c', 'd']
'''
dict1= dict(a=1,b=2,c=3)
dict1['d']='4'
print(dict1)
del dict1['b']
print(dict1)
dict1['a']='5'
print(dict1)
if 'c' in dict1:
 print('true')
else:
 print('false')
print(dict1.keys())
