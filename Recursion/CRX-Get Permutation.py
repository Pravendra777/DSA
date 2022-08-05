def permutation(n):
    if len(n)==0:
        return [""]
    
    ch=n[0]
    ros=n[1:]
    rr=permutation(ros)
    mr=[]
    for i in rr:
        for j in range(len(i)):
            mr.append(i[:j]+ch+i[j:])
        
print(permutation("abc"))