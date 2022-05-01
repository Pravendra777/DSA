def re(arr,start,end):
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end] = temp
        start += 1
        end = end-1
    



arr=[1,2,3,4,5]
start=0
end=len(arr)
re(arr,start,end-1)
print(arr)