def issorted(arr,le):
    if len(arr)-1 == le:
        return True
    if arr[le]>arr[le+1]:
        return False
    return issorted(arr,le+1)
def main():
    arr = [1,2,3,4,5,6,7,8,0,9]
    print(issorted(arr,0))
if __name__ == '__main__':
    main()  