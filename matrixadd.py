x=[[1,2,3],[1,2,3],[1,2,3]]
y=[[1,2,3],[1,2,3],[1,2,3]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
                   r[i][j]=x[i][j]+y[i][j]
for z in r:
    print(z)                  
                   
