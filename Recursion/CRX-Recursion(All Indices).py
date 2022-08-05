result=[]
def find(arr,n,x):
    if len(arr)==n:
        return
    if arr[n]==x:
        result.append(n)
    find(arr,n+1,x)
def main():
    arr = [1,2,3,4,5,6,4,4,9,10]
    find(arr,0,4)
    if len(result)==0:
        print("Not Found")
    else:
        print(result)
if __name__ == '__main__':
    main()