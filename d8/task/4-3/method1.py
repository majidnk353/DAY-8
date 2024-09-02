num=int(input("enter a number:"))
i=0
c=[]
for i in range(1,num*10+1):
        if(i<11):
          i*=num
          c.append(i)
print(c)
