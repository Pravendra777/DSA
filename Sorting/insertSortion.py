def insertionsort(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        j = i-1  
        while j >= 0 and key < lst[j] :  
                lst[j + 1] = lst[j]  
                j = j-1  
        lst[j + 1] = key
    return lst 
lst=[10,20,3,4,2,1]
print(insertionsort(lst))