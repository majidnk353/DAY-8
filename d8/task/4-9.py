x=[4,5,3,2,1,6,2]
y=[9,8,7,5,4,6,8]
z=[]
for i in range(len(x)):
    for j in range(len(y)):
                   if(x[i]==y[j]):
                      z.append(x[i])
print(z)
        
