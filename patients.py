age=[]
n=int(input("enter no of patients:"))
if n>0 and n<=20:
    for i in range (n):
        age.append(int(input("enter age of patient:")))
    fees=0
    for ages in age:
        if ages<=0 or ages>120:
            print("invalid age")
        
        elif ages<17:
            fees+=200
        elif ages>=17 and ages<=40:
            fees+=400
        else:
            fees+=300
    print("Total fees collected:", fees)