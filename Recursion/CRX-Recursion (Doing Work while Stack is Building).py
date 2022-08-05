def sysout(n):
    if n == 0:
        return
    print(n)
    sysout(n-1)
sysout(5)