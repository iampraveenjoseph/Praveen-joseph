n=int(input("enter the number "))
flag=0
for i in range(2,n//2):
    if(n%i==0):
        flag=1
        break
if(n==1):
    print("1 is either composite or nor a prime")
else:
    if flag==0:
        print(n,"is prime")
    else:
        print(n,"it is not a prime")
