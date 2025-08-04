a=int(input("enter the no. of numbers in list:"))
c=[]
ev=[]
for i in range(a):
    b=int(input("enter the number:"))
    c.append(b)
    if b%2==0:
        ev.append(b)
print("Original list: ",c)
print("even list: ",ev)