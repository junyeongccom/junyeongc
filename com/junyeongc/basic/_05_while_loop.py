# ***********************
# -- 반복문
# ***********************

# while loop

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

# The Infinite Loop

var = 1
while var == 1 :  # This constructs an infinite loop
   num = int(input("Enter a number  :"))
   print ("You entered: ", num)

print ("Good bye!")

# Using else Statement with Loops

count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

# Single Statement Suites
flag = 1
while (flag): print ('Given flag is really true!')
print ("Good bye!")
''' 
The above example goes into an infinite loop and you need to press CTRL+C keys to exit.
'''