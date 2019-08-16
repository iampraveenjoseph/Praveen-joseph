from pythonds.basic import Queue
def hotline(namelist,num):
    s=Queue()
    for name in namelist:
        s.enqueue(name)
    #return s.size()
    while s.size()>1:
        for i in range(num):
            s.enqueue(s.dequeue())
            s.dequeue()
            return s.dequeue()
print(hotline(["hello","i","am","praveen","joseph"],5))
