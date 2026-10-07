lst = ['apple','banana','cherry','date','elderberry']
print(lst)

print(lst[0])
print(lst[4])
print(lst[-4])

print(lst[1:4])
print(lst[1:5:2])

if 'cherry' in lst:
    print("Yes")
else:
    print("No")

list = [i*i for i in range(0,10)]
print(list)

lst1 = [i*i for i in range(0,10) if i%2==0]
print(lst1)