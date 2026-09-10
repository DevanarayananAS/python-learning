T=int(input("Enter time in hours"))
E=[]
L=[]
for i in range(T):
  E.append(int(input()))
for i in range(T):
  L.append(int(input()))
g=0
max=0
for i in range(T):
  g+=(E[i]-L[i])
  if max<g:
    max=g
print(max)