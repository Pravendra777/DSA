def palin(arr):
    if len(arr)<2:
        return True
    if arr[0]!=arr[-1]:
        return False
    return palin(arr[1:-1])
arr="hello"
print(palin(arr))