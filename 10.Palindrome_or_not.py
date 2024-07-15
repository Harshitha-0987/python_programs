n=int(input())
sum=0
a=n
while(n!=0):
    rem=n%10
    if(a==sum):
        print("palindrome")
    else:
        print("not a palindrome")
