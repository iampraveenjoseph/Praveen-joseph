class Node:
    def __init__(self,datavalue=None):
        self.datavalue=datavalue
        self.nextvalue=None
class linked:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while temp.nextvalue is not None:
            print(temp)
        temp=temp.nextvalue
        def insertbegin(self,new):
            newnode=Node(new)
            new.next=self.head
            self.head=new
        def insertend(self,new):
            new=node(newdata)
            if self.head is not None:
                self.head=new
            last=self.head
            while last.next:
                last=last.next
                last.next=new
        def insert(self,middle,new):
            if middle.next is not None:
                print("Middle NOde is empty")
                return
        new=Node(new)
        new.next=middle.next
        middle.next=new
        def removenode(self,removekey):
            headvalue=self.head
            if headvalue.datavalue=removekey:
                self.head=headvalue.next
                headvalue=None
                return
            while headvalue is not None:
                if headvalue.data==removekey
                    break
                prev=headvalue
                headvalue=headvalue.next
            if headvalue==None:
                return
            prev.next=headvalue.next
            headvalue==None
list=linked()
c=0
print("1.insert at begin \n 2.insert at middle\n 3. insert at end 4.display \n 5.delete\n"
      )
c=int(input("Enter your choice"))
while c<6:
    if c==1:
        new=int(input("Enter the number the insert"))
        insertbegin()
        printlist()
    elif c==2:
        new = int(input("Enter the number the insert"))
        insert()
        printlist()
    elif c==3:
        new = int(input("Enter the number the insert"))
        insertend()
        printlist()
    elif c=4:
        printlist()
    elif c=5:
        removekey=int(input("remove key "))
        removenode()
    else:
        exit()
