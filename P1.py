count=0
n=int(input("Enter digit:"))
while n!=0:
    n//=10                          #Count of digits
    count+=1
print("Count of the number is:"+str(count))

fact=1
n=int(input("Enter number:"))
for i in range(1,n+1,1):                ##Fact
    fact=fact*i
print("Factorial of number is:",fact)


num = int(input("Enter number:"))     #reverse a number
reverse = int(str(num)[::-1])
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

s=input('Enter a string:')
rev=s[::-1]
print("Reversed String is:",rev)

n=int(input("Enter number:"))
if n==1:
    print(n,"is not a prime number")
elif n>1:
    for i in range(2,n):
        if(n%i)==0:                 #prime
            print("Not Prime")
            break
    else:
        print("Prime Number")
    
lower=1
upper=100
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
                break
       else:
           print(num)


sample_str = "P@yn2at&#i5ve"
c_count=0
d_count=0
s_count=0
for char in sample_str:
    if char.isalpha():                    #count digit,char,symbols
        c_count += 1
    elif char.isdigit():
        d_count += 1
    else:
        s_count += 1
print("Chars =", c_count, "Digits =", d_count, "Symbol =", s_count)

a=input('Enter string:')
consonants=0;vowels=0;
for i in a:
    if(i=='a' or i=='e' or a=='i' or a=='o' or a=='u' or
       i=='A' or i=='E' or a=='I' or a=='O' or a=='U'):
        vowels=vowels+1
    else:
        consonants=consonants+1
print(f'Vowels={vowels} and consonants={consonants}')

x1=float(input("Enter x1 of x coordinate:"))
y1=float(input("Enter y1 of y coordinate:"))
x2=float(input("Enter x2 of x coordinate:"))
y2=float(input("Enter y2 of y coordinate:"))
d=((x2-x1)**2 + (y2-y1)**2)**0.5
print(d)

cp=float(input("Enter cost price:"))
sp=float(input("ENter selling price:"))
if cp>sp:
     amt=cp-sp
     print("Loss=",amt)
else:
     amt=sp-cp
     print("Profit",amt)


a=int(input("Enter a two digit number:"))
rev=(a%10)*10 + a//10
print("Reverse is:",rev)

num=int(input("Enter 3 digit number:"))
a=num%10  #345%10=5
num=num//10 #345//10=34
b=num%10  #34%10=4
c=num//10  #34//10=3
res=a*100+b*10+c
print('Reverse is:',res)

#find median
a=int(input('Enter no 1:'))
b=int(input('Enter no 2:'))
c=int(input('Enter no 3:'))
if a>b:
    if a>c:
        print('Median is',a)
elif b>a:
    print('Median is',b)
else:
    print('Median is',c)

n=input('Enter a nos:')
l=list(n)
print(max(l))

a=0;b=1;c=0;
n=int(input('Enter number:'))
print('\nFibonacci series')
print(a); print(b);
for i in range(1,n-1):              #Fibonacci
    c=a+b
    print(c)
    a=b
    b=c

sum=0
x=int(input('Enter digit:'))
copy=x
while x!=0:
    digit=x%10
    sum=sum+digit**3                        #Armstrong
    x=x//10
if sum==copy:
    print("Armstrong")
else:
    print('Not an armstrong')

import cmath
a=float(input("Enter number:"))
b=float(input("Enter number:"))
c=float(input("Enter number:"))
d=(b**2)-(4*a*c)
x=(-b-cmath.sqrt(d))/(2*a)
y=(-b+cmath.sqrt(d))/(2*a)
print(f"The solution are {x} and {y}")

a=10; b=20
print('Before swapping:',a,b)
a=a+b #30
b=a-b  #10
a=a-b  #20
print('After swapping:',a,b)