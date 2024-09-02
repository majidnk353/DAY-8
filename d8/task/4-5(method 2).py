#fibinacci sequence
num=int(input("enter the number:"))
for i in range(num):
    print(i)
    if(i==1):
        print(i)
    i=i+(i-1)
    print(i)
