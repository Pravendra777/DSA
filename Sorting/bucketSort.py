def insertionsort(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        j = i-1  
        while j >= 0 and key < lst[j] :  
                lst[j + 1] = lst[j]  
                j = j-1  
        lst[j + 1] = key
    return lst 
def bucketSort(x):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
     
    for i in range(slot_num):
        arr[i] = insertionsort(arr[i])
         
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x

x = [0.967, 0.165, 0.692,
     0.294, 0.572, 0.453]
print("Sorted Array is")
print(bucketSort(x))