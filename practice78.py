m=int(input("enter your first number:"))
n=int(input("enter your second number:"))

for i in range(m,n):
    for j in range(m,n):
     z=i*j
     print(z,end =" \t")
    print()