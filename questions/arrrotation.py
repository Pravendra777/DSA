def array(arr,n,d):
    k=arr.index(d)
    x=arr[k+1:]+arr[:k+1]
    return x
arr=[1,2,3,4,5]
n=5
d=1
print(array(arr,n,d))