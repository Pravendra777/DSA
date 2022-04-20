def opt(arr,num):
    for i in range(len(arr)-1):
        if arr[i]==num:
            return "element find on left"+str(i)
            break
        if arr[(len(arr)-1)-i]==num:
            return "element find on " +str((len(arr))-i)
            break
    return "no element found"

arr=[2,1,3,4,5,6,8,2,3,4,5,6,4]
num=4
print(opt(arr,num))        