def toh(arr,n,from_,to,temp):
    if n==0:
        return
    toh(arr,n-1,from_,temp,to)
    print("Move",arr[n],"from",from_,"to",to)
    toh(arr,n-1,temp,to,from_)
arr=[1,2,3]
n=len(arr)
toh(arr,n,"sur","dest","hel")
