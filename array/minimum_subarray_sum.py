def subarr(arr):
    min=999999999
    cur=0
    for i in range(1,len(arr)):
        cur+=arr[i]
        if cur<min:
            min=cur
        if cur<0:
            cur=0
    return cur
        




a=int(input())
b=list(map(int,input().split()))
c=subarr(b)
print(c)