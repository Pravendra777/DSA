def fect(n):
    if n==1:
        return 1
    return n*fect(n-1)
print(fect(5))