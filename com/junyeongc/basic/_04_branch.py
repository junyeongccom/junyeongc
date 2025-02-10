# ***********************
# -- 비교문
# ***********************
# Single Statement Suites
var = 100
if ( var  == 100 ) : 
    print ("Value of expression is 100") # Value of expression is 100
print ("Good bye!") # Good bye!

# The else Statement
amount = int(input("Enter amount: "))

if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
else:
   discount = amount*0.10
   print ("Discount",discount)
    
print ("Net payable:",amount-discount)

#The elif Statement

amount = int(input("Enter amount: "))

if amount<1000:
   discount = amount*0.05
   print ("Discount",discount)
elif amount<5000:
   discount = amount*0.10
   print ("Discount",discount)
else:
   discount = amount*0.15
   print ("Discount",discount)
    
print ("Net payable:",amount-discount)