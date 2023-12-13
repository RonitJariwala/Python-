list=[[1,2,3],[2,5,6],[8,7,5]]
print(list)
print("Rows",len(list))
print("Columns",len(list[0]))
print(list[0][0],list[0][1],list[0][2])
print(list[1][0],list[1][1],list[1][2])
print(list[2][0],list[2][1],list[2][2])


my_list=[1, 2, 3, 4, 5]
list_sum=sum(my_list)
max=max(my_list)
min=min(my_list)
print("Sum of items in the list:", list_sum)
print(f"Maximum and minimum is {max} and {min}")

key=[1,2,3]
value=[1,4,8]
newdict=dict(zip(key,value))
print(newdict)

a='organisation'
count=0
for i in a:
    if i=='o':
        count=count+1
print("count of o is",count)

a=3;b=4
c=(a**2+b**2)**0.5
print(c,"is the 3rd side")

x=[1,2,3,4,5,6,7,8,9,10]
newList=[x for x in range(1,11) if x%2==0]
print(newList);

x=[10,20,30,40,50]; sum=0;
for i in x:
        sum=sum+i
avg=sum/len(x)
print(f"Sum={sum} and average={avg}")

fruits=['apple','cherry','banana','coco','mango','grapes']
new=[]
for i in fruits:
     if 'c' in i:
          new.append(i)
print(new)

l=[1,2,'apple',[12,'mango']]
print(l)
l[3][1]='pineapple'
print("New=",l)

l=[1,2,'banana',3,4,'apple']
if 'apple' in l:
     print('yes')
else:
     print('no')
l.append('orange')
l.insert(1,6)
l.remove(4)
print(l)