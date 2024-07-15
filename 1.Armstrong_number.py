n=int(input())
sum=0
a=n
while(n!=0):
    rem=n%10
    sum=sum+remrem*rem*rem
    n=n/12
if(a==sum):
    print(" ")
else:
