# ***********************
# -- 리스트 검색
# ***********************
no = int(input('any number: '))
numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num == no:
      print ('number found in list')
      break
else:
   print ('number not found in list')

''' 
any number: 33
number found in list

any number: 5
number not found in list
'''