# skillcaptainpython
Variable is a reusable container for storing a value .<br />
A variable behaves as if it were the value it contains.<br />
Data types in python:<br />
int: Represents whole numbers without decimal points. It could be negative or positive.<br />
float: Represents decimal numbers. Simply numbers with a fractional part.<br />
str: Represents sequences of characters (text!).<br />
bool: Represents logical values, True or False.<br />
list: Represents ordered collections of elements.<br />
tuple: Represents ordered but not so changable collections of elements.<br />
dict: Represents key-value pairs in a dictionary.<br />
set: Represents unordered collections of unique elements.<br />
byte: Represents a sequence of bytes, typically used for storing binary data.
<br />
Just try to remember the name and you will be able to learn where they are used as you will be using them. <br />

Operators <br />
Operators are used to perform operations on values or variables. Python provides various types of operators, including arithmetic, comparison, logical, assignment, and more.
<br />
Arithmetic Operators:<br />
Addition (+): Adds two values.
Subtraction (-): Subtracts one value from another.
Multiplication (*): Multiplies two values.
Division (/): Divides one value by another.
Modulus (%): Returns the remainder of division.
Exponentiation (**): Raises a value to a power.
Floor Division (//): Returns the integer quotient of division.
<br />
Comparison Operators:<br />
Equal to (==): Checks if two values are equal.
Not equal to (!=): Checks if two values are not equal.
Greater than (>): Checks if the left value is greater than the right value.
Less than (<): Checks if the left value is less than the right value.
Greater than or equal to (>=): Checks if the left value is greater than or equal to the right value.
Less than or equal to (<=): Checks if the left value is less than or equal to the right value.
<br />
Logical Operators:<br />
And (and): Returns True if both operands are True.
Or (or): Returns True if either of the operands is True.
Not (not): Returns the opposite of the operand's logical value.
<br />
Assignment Operators:<br />
Assigns a value to a variable. Example: x = 5
<br />
Condition:<br />
Conditions allow you to control the flow of your program based on certain criteria. In Python, conditions are expressed using if, elif, and else statements.
<br />

    if condition1:
        # code to be executed if condition1 is true
    elif condition2:
        # code to be executed if condition2 is true but condition1 is not true
    elif condition3:
        # code to be executed if condition3 is true but condition1 and condition2 are not true
    else:
        # code to be executed if none of the conditions are true
<br />
In conditions, you can use comparison operators (==, !=, <, >, <=, >=) to compare values, logical operators (and, or, not) to combine conditions, and other techniques to make complex comparisons.
<br />
Example:
<br />

    if 2 != 2:
    	print("This is stupid")
    else:
    	print("Not so stupid!!")
  <br />   
  Loops: while and for loops
  <br />   
Loops are used in Python to execute a block of code repeatedly until a certain condition is met. Two commonly used loops in Python are the while loop and the for loop.  <br />   

while loop: The while loop executes a block of code as long as a specified condition is true.  <br />   

Example:  <br />  

    
    count = 0
    while count < 5:
        print("Count:", count)
        count += 1
  <br />       
for loop: The for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects.
  <br />   
  
Example:  <br />  
    
        numbers = [1, 2, 3, 4, 5]
        for num in numbers:
            print("Number:", num)
    
  <br />  
You can use control statements like break and continue to modify the behavior of loops. The break statement is used to exit the loop prematurely, and the continue statement is used to skip the rest of the loop iteration and move to the next one.
  <br />  

 Exceptionss:  <br />  
 an exception is an eventdetectedduring execution that interrupts the normal flow of a program <br />  
 Handling this exception using arbitrary functions and commands is known as exception handling.   <br /> 
 
```
 try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")
```
Defining Functions in python:  <br />  
A Python function is like a named recipe or set of instructions that you can use again and again. It allows you to group a series of statements together and give them a name.  <br />  

Whenever you need to perform a specific task, you can simply call the function by its name to execute those instructions.
  <br />  
Example:

    # Define a function named "add_numbers" that adds two numbers
    def add_numbers(num1, num2):
        result = num1 + num2
        return result

    # Call the function and pass two numbers
    sum = add_numbers(3, 5)
    print(sum)  # Output: 8

Array and List: <br />  
In Python, arrays and lists are both used to store multiple values, but they have some key differences:<br />  
Lists:<br />  
- Lists are a built-in data structure in Python<br />  
- They can hold elements of different data types, such as integers, floats, strings, and even other lists.<br />  
- Lists are mutable, meaning you can modify their elements after they are created.<br />  
- They are defined using square brackets [] and elements are separated by commas.<br />  
Example:<br />  
```
    my_list = [1, 2, "hello", 3.14, [4, 5, 6]]
```

Arrays:<br />  
- Arrays, on the other hand, are a data structure provided by the `array` module in Python's standard library.<br />  
- Unlike lists, arrays can only hold elements of the same data type, typically numbers (integers or floats).<br />  
- Arrays are generally more memory efficient and faster for numerical computations than lists.<br />  
- They are defined using the `array` function from the `array` module, specifying the data type and the initial elements.<br />  

Example:<br />  
```
    import array

    my_array = array.array('i', [1, 2, 3, 4, 5])
```

In most cases, you'll likely use lists more frequently because of their flexibility. However, if you are working with large amounts of numerical data and performance is a concern, arrays can be a suitable choice.<br />  

It's important to note that arrays require importing the `array` module, while lists are available by default in Python.<br />  

Dictionary:<br />  

A dictionary in Python is a collection of key-value pairs, where each key is unique within the dictionary. It is a mutable data structure that allows you to store and retrieve values based on their associated keys.<br />  

Here's a brief explanation of dictionaries in Python:<br />  

Declaration: Dictionaries are defined using curly braces {} or the dict() constructor. The key-value pairs are written as key: value separated by commas.<br />  

    # Using curly braces
    my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

    # Using the dict() constructor
    my_dict = dict(name='John', age=25, city='New York')

Accessing Values: You can access the value associated with a specific key by using the key inside square brackets `[]`.<br />  

    print(my_dict['name'])  # Output: John
    print(my_dict['age'])   # Output: 25

Modifying Values: You can modify the value associated with a key by assigning a new value to that key.<br />  

    my_dict['age'] = 30
    print(my_dict['age'])   # Output: 30

Adding and Removing Key-Value Pairs: You can add a new key-value pair by assigning a value to a new key, and you can remove a key-value pair using the `del` keyword.<br />  

    my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
    del my_dict['city']                 # Removing a key-value pair

Dictionary Methods: Dictionaries have various built-in methods that allow you to manipulate and retrieve information from dictionaries. Some common methods include `keys()`, <br />  `values()`, `items()`, `get()`, `pop()`, and `clear()`.

    print(my_dict.keys())    # Output: ['name', 'age', 'occupation']
    print(my_dict.values())  # Output: ['John', 30, 'Engineer']
    print(my_dict.items())   # Output: [('name', 'John'), ('age', 30), ('occupation', 'Engineer')]

Dictionaries are useful when you need to store and retrieve data based on unique keys. They are often used to represent real-world entities or to store configurations and settings.<br />  
