def bubble_sort(lst):
    for i in range(len(lst)):
        count=0
        swap=0
        for j in range(0,(len(lst)-i)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                swap=1
                count+=1
        if swap==0:
            print("no swapping for ",i+1,"iteration , list has been sorted in ",i,"iteration")
            break
        print("sawp for", i+1,"iteration","=",count)
        count=0
    return lst
lst=[3,2,1,6,4]
print(bubble_sort(lst))