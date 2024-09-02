x=[1,2,3,4,5,7]
max=x[0]
for i in range(1,len(x)):
    if max < x[i]:
        max = x[i] 
print(max)
