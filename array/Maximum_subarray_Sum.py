def subarr(arr):
    cur=arr[0]
    ovr=arr[0]
    for i in range(1,len(arr)):
        if cur>0:
            cur+=arr[i]
        else:
            cur=arr[i]
        if cur>ovr:
            ovr=cur
    return ovr






a=int(input())
b=list(map(int,input().split()))
c=subarr(b)
print(c)