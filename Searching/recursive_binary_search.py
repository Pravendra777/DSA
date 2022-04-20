def rebin(low,high,arr,num):
    if high >= low:

        mid = low + (high - low)//2

        
        if arr[mid] == num:
            return mid

        elif arr[mid] > num:
            return rebin(low,mid-1,arr,num)

        
        else:
            return rebin(mid+1,high,arr,num)
    else:
        return -1


arr=[3, 4, 5, 6, 7, 8, 9]
num=5
print(rebin(0,len(arr)-1,arr,num))
