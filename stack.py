class stack:
    def __init__(self):
        self.stack=[]
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def peek(self):
        if len(self.stack)<=0:
            print("No element is to display")
        else:    
            return self.stack[-1]
    def remove(self):
        if len(self.stack)<=0:
            return("No value found")
        else:
            return self.stack.pop()
a=stack()
c=0
while c!=4:
    print("1.PUSH\n2.PEEK\n3.POP")
    c=int(input("enter the choice:"))
    if c==1:
        data=input("enter the data to be add:")
        a.add(data)
        print(a.peek())
    elif c==2:
        print(a.peek())
    elif c==3:
        print(a.remove())
    else:
        print("invalid choice")
        exit()
        
