def linear(arr,val):
    x=0
    for i in arr:
        if val==i:
            return x+1
            break
        x+=1
    return 0
a=[2,3,4,1,2,5]
print(linear(a,1))