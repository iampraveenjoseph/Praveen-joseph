dic={"a":1,"b":2}
dic2={"c":3,"d":4}
d=dic.copy()
d.update(dic2)
print(d)
print(sum(d.values()))
 
