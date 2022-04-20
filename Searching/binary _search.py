def bin(arr,low,high,num):
    while(low<=high):
        mid= low + (high - low)//2
        if arr[mid]==num:
            return "found"
            break
        elif arr[mid]<num:
            low=mid+1
        else:
            high=mid-1
    return "not found"
arr=[3, 4, 5, 6, 7, 8, 9]
num=5
print(bin(arr,0,len(arr)-1,num))