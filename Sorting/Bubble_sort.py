def bubble_sort(lst):
    count=0
    for i in range(len(lst)):
        for j in range(0,(len(lst)-i)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                count+=1
        print("sawp for", i+1,"iteration","=",count)
        count=0
    return lst
lst=[3,2,1,6,4]
print(bubble_sort(lst))