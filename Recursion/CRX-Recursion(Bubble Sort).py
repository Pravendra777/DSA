def bubble(arr,si,le):
    if le==0:
        return
    if si==le:
        bubble(arr,0,le-1)
        return
    if arr[si]>arr[si+1]:
        arr[si],arr[si+1]=arr[si+1],arr[si]
    bubble(arr,si+1,le)



def main():
    arr = [6,7,8,9,10,1,2,3,4,5]
    bubble(arr,0,len(arr)-1)
    print(arr)
if __name__ == '__main__':  
    main()