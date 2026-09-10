s1,s2,s3=input("enter three words:").split()
v='aeiouAEIOU'

for char in v:
    s1=s1.replace(char,'%')

for char in s2:
    if char not in v:
        s2=s2.replace(char,'#')

s3=s3.upper()
print(s1+s2+s3)