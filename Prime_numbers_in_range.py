n=int(input())
count=0
for i in range(1,n+1):
    count=0
    for i in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i)
