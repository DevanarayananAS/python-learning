r=int(input("enter no of rows:"))
c=int(input("enter no f columns"))
max=0
for i in range(r):
    sum=0
    for j in range(c):
        sum+=int(input())

    if sum>max:
        max=sum
        index=i
print(index)