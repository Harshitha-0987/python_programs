arr=[1,2,3,4,5,6,7]
n=len(arr)
countEven=0
countOdd=0
for i in range(0,n):
    if(arr[i]%2==0):
        countEven+=1
    else:
        countOdd+=1
print("even elments:",countEven)
print("odd elements:",countOdd)
