# ***********************
# -- 서포트
# ***********************
def print_func( x ):
   print("Hello : ", x)
   return

def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result