s=int(input("start "))
l=int(input("end "))
for n in range(s,l+ 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
