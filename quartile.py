# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def q1(n,number):
    number=sorted(number)
    a=(n+1)/4
    frac, whole = math.modf(a)
    whole=int(whole)
    return number[whole-1]+(frac*(number[whole]-number[whole-1]))


def q2(n,number):
    b=(n+1)/2
    number=sorted(number)
    frac, whole = math.modf(b)
    whole=int(whole)
    return number[whole-1]+(frac*(number[whole]-number[whole-1]))


def q3(n,number):
    c=(3*(n+1))/4
    number=sorted(number)
    frac, whole = math.modf(c)
    whole=int(whole)
    return number[whole-1]+(frac*(number[whole]-number[whole-1]))

n = int()
number = [3,7,8,5,12,14,21,15,18,14]
n=10
number1=sorted(number)
print(number1)
print(math.ceil(q1(n,number1)))
print(math.ceil(q2(n,number1)))
print(int(q3(n,number1)))