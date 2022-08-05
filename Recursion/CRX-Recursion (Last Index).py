mu=[]
def last(arr,le,nums):
    if arr[le]==nums:
        mu.append(le)
    if le==len(arr)-1:
        return mu
    return last(arr,le+1,nums)
def main():
    arr = [1,2,3,4,5,6,7,8,5,10]
    dum=last(arr,0,0)
    if len(dum)==0:
        print("Not Found")    
    else:
        print(dum[-1])
if __name__ == '__main__':
    main()

