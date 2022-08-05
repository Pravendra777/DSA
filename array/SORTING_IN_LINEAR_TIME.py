a=int(input())
b=list(map(int,input().split()))
low=0
mid=0
high=len(b)-1
while mid<=high:
    if b[mid]==0:
        x=b[mid]
        b[mid]=b[low]
        b[low]=x
        low+=1
        mid+=1
    elif b[mid]==1:
        mid+=1
    else:
        x=b[mid]
        b[mid]=b[high]
        b[high]=x
        high-=1
print(b)