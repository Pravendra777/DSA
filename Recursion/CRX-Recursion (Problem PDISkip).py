def sysout(n):
    if n==0:
        return 
    if n%2==1:
        print(n)
    sysout(n-1)
    if n%2==0:
        print(n)
sysout(5)