def arrayreverse(arr,start,end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
def leftrotate(arr,n,d):
    if d==0 or n<2:
        return
    d=d%n
    arrayreverse(arr,0,d-1)
    arrayreverse(arr,d,n-1)
    arrayreverse(arr,0,n-1)
arr=[1,2,3,4,5,6]
n=6
d=2
leftrotate(arr,n,d)
print(arr)