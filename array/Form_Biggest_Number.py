a=int(input())
b=list(map(str,input().split()))
for i in range(len(b)-1):
    for j in range(i+1,len(b)):
        if b[i]+b[j]<b[j]+b[i]:
            b[i],b[j]=b[j],b[i] # swap  
print(b)
