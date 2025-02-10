# ***********************
# -- 연산자
# ***********************
''' 
Python language supports the following types of operators −

Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators
'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True 
''' because z is the same object as x '''
print(x is y) # returns False 
''' because x is not the same object as y, even if they have thew same content '''
print(x == y) #  this comparison returns True
'''  
to demonstrate the difference betweeen "is" and "==":
because x is equal to y 
'''