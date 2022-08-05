def pattern(n):
    if n==0:
        return 
    pattern(n-1)
    print("*"*n)
def main():
    pattern(5)

if __name__ == '__main__':
    main() 