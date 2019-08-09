n =int(input("enter the number to find factorial "))
fact = 1
for i in range(1,n+1): 
    fact = fact*i 
print ("The factorial of ",end="") 
print (fact) 
