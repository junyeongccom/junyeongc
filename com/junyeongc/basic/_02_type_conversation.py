# ***********************
# -- 타입 변환
# ***********************
# to int
a_float = 3.3
b_float = 2.0

# Explicit type conversion from float to int
c_int_sum = int(a_float + b_float) 
print(c_int_sum)  # 5

c_float_sum = a_float + b_float
print(c_float_sum) # 5.3

# to str
price_cake = 15
price_cookie = 6
total = price_cake + price_cookie
''' print("The total is: " + total  + "$") ''' # TypeError 
print("The total is: " + str(total)  + "$") # The total is: 21$

# to tuple, to list

a_tuple = (1,2,3,4,5,6,7,8,9,10)
b_list = [1,2,3,4,5]

print(tuple(b_list))  # (1, 2, 3, 4, 5)
print(list(a_tuple)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

''' You can also convert a string into a list or a tuple. '''

dessert = 'Cake'

# Convert the characters in a string to individual items in a tuple
print(tuple(dessert)) # ('C', 'a', 'k', 'e')

# Convert a string into a list
dessert_list = list(dessert) 
dessert_list.append('s')
print(dessert_list)  # ['C', 'a', 'k', 'e', 's']