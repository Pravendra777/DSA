def sysout(n):
    if n==0:
        return
    
    sysout(n-1)
    print(n)
sysout(5)