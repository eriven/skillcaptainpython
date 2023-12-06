#Develop a Python program to perform conversions between a list and a set, adhering to the following requirements:
# 1. Define a list with some elements.
# 2. Design a function that converts the list into a set.
 #3. Design another function that converts a set into a list.
 #4. Print both the converted list and set.

# Step 1: Define a list with some elements
my_list = [1, 2, 3, 4, 5, 5, 6, 7, 7]

# Step 2: Design a function that converts the list into a set
def list_to_set(input_list):
    return set(input_list)

# Step 3: Design another function that converts a set into a list
def set_to_list(input_set):
    return list(input_set)

# Converting list to set and printing
converted_set = list_to_set(my_list)
print("Converted Set:", converted_set)

# Converting set back to list and printing
converted_list = set_to_list(converted_set)
print("Converted List:", converted_list)
