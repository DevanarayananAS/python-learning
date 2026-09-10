str=input("enter a string of any length:")
a=0
b=0
for char in str:
    if char == '*':
        a+=1
    elif char == '#':
        b+=1
print(a-b)
        




    #or


s=input("enter a string of any length:")
a=s.count('*')
b=s.count('#')
print(a-b)
