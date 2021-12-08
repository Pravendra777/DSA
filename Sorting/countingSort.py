def countingSort(arr):
    m =max(arr)
    count = [0] * (m+1)

   
    for el in arr: 
        count[el] += 1

    
    for i in range(1, m+1):
        count[i] += count[i-1] 

   
    out = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        currentEl = arr[i]
        count[currentEl] -= 1
        newPosition = count[currentEl]
        out[newPosition] = currentEl
        i -= 1

    return out

arr = [4,4,2,1,5,4,6,9]
print("Input array = ", arr)

sortedArray = countingSort(arr)
print("Counting sort result = ", sortedArray)