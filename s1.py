
str="LIONELMESSI"
length=len(str)           
mid=int(length/2)
r=str[mid]
print(r)

str1="JhonDipPeta"
print("Original String is", str1)
mi=int(len(str1) / 2)                       #Get middle 3 characters
res=str1[mi - 1:mi + 2]
print("Middle three chars are:",res)


s1="Sita"
s2="Rama"
print("Original strings are", s1, s2)
mi=int(len(s1)/2)
x=s1[0:mi]                               #Middle insertion
x=x+s2
x=x+s1[mi:]
print("After appending new string in middle:", x)

str="HihelloHow"
print('Qg String',str)
lower=[]
upper=[]
for char in str:              #Lower comes First
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
str1=''.join(lower+upper)
print("Result=",str1)


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

str1 = "Apple"
char_dict = dict()
for char in str1:
    count = str1.count(char)    #count of chars
    char_dict[char] = count
print('Result:', char_dict)

"""
input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:         #count sum and avg of digits
    if char.isdigit():
        total += int(char)
        cnt += 1
avg = total / cnt
print("Sum is:", total, "Average is ", avg)


str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)
res = "".join([item for item in str1 if item.isdigit()])  #seperate int
print(res)


import string
str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)
replace_char = '#'                               
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)               #replace #
print("The strings after replacement : ", str1)
"""

a='organization'
print(a)
print(a[0:5])
print(a[::-1])