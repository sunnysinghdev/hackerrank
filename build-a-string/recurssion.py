import sys
#sys.setrecursionlimit(40000)
counter = 0
def factorial(n):
    global counter
    counter+=1
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

def factorialTR(n, a):
    #global counter
    print(a)
    #counter+=1
    if n==0 or n==1:
        return a
    return factorialTR(n-1, a+1)

val = 4000
counter = 0
#n = factorial(val)
n = factorialTR(val, 0)
print(counter, n)