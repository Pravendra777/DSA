def first(arr,le,num):
    if len(arr)== le:
        return -1
    if arr[le]==num:
        return le
    return first(arr,le+1,num)
def main(): 
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(first(arr,0,0))   
if __name__ == '__main__':  
    main()