d={"a":1,"b":2,"c":3,"d":4}
d1={"c":2,"d":2}
for i in d:
    if i in d1:
        d[i]+=d1[i]
        print(d[i])
