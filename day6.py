#Design a Python program to execute division on two predefined numbers, 
#while considering the possibility of a division by zero error.
#Ensure that the program handles this exception gracefully, providing a clear error message in such cases.
num=int(input("Enter numerator"))
den=int(input("Enter denominator"))
try:
 div=num/den
except ZeroDivisionError:
 print("Division by zero is not allowed.")
else:
 print(div)
