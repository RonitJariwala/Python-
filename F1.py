def fact(n):
    if n==0: return 1
    return n * fact(n-1)
print(fact(5))

def add(n):
    if n:
        return n + add(n-1)
    else: 
        return 0
print(add(3))

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input('Enter number'))
for i in range(n+1):
    print(fibo(i))

def pal(s):
    s=s.lower()
    return s==s[::-1]
string=input('Enter a string')
if pal(string):
    print(string,'is palindrome')
else:
    print(string,'is not a palindrome')

def add1(n):
    return n+10
def mult1(n):
    return n*add1(n)
print(mult1(10))

sub_marks=[('Eng',78),('Science',89),('Maths',97),('Social Science',81)]
print("Original List of tuples")
print(sub_marks)
sub_marks.sort(key=lambda x:x[1])
print("\nSorting the list of tuples:")
print(sub_marks)

num=[1,2,3,4,5]
print('Original list=',num)
print('\nSquare of nums:')
sq_num=list(map(lambda x : x**2,num))
print(sq_num)
print('\nCube of nums:')
cub_num=list(map(lambda x : x**3,num))
print(cub_num)

n1=[2,5,6]; n2=[4,6,7]
print(n1,n2)
res1=list(map(lambda x,y : x-y,n1,n2))
print("\nAfter addition result is:",res1)
res2=list(map(lambda x,y : x-y,n1,n2))
print('\nAfter substraction result is:',res2)

from functools import reduce
def multiply(x, y):
    return x*y
product=reduce(multiply,range(1, 101))
print("Product of numbers from 1 to 100%:", product)

a=[1,2,3,4,5,6,7,8]
print('Og arrays:',a)
even=list(filter(lambda x:x%2!=0,a))
odd=list(filter(lambda x:x%2==0,a))
print(f'Even={even} and odd={odd}')


n1=[1,2,3,5,7]; n2=[5,9,8,4];
print('Og Arrays')
print(n1,n2)
res=list(filter(lambda x: x in n1,n2))
print('\nIntersection of list:',res)

num=[2,4,6,8]; n=2
print('Og list=',num)
a=list(map(lambda x: x*n,num))
print('New list=',a)

n1[1,2,3]
print('Og list is:',n1)
res=list(map(lambda x:x+x+x,n1))
print('Triple of said list numbers:',res)

color=['Red','Blue','Black','White','Pink'] 
print("Original list:")
print(color) 
print("\nAfter listify the list of strings are:") 
result=list(map(list, color)) 
print(result)

def change_case(s):
    return str(s).upper(),str(s).lower()
chars={'a','b','E','f','a','i','o','U','a'}
print('Original Chars',chars)
res=set(map(change_case,chars))
print('\nAfter conversion we get:',res)


def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i += 6
    return True
n=[1,2,3,4,5,6,7,8,9]
print('List of integers:',n)
prime=list(filter(isPrime,n))
print('\nPrime numbers from list are:',prime)

def outer(x):
    def inner(y):
        return x+y
    return inner
x=outer(7)
sum=x(5)
print(sum)