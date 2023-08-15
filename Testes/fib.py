def fib(n):
    if n < 2: 
        return n                             
    else: 
        return fib(n - 1) + fib(n - 2) 

print(fib(int(input())))

'''
def fat(n):
  if n < 2:
    return 1
  else:
    return n * fat(n - 1)
print(fat(int(input())))
'''