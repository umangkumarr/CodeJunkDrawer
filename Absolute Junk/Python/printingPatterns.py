def printingpattern(n):
    for i in range(n,0,-1):
        l=[]
        for j in range(n,0,-1):
            if j>i:
                l.append(j)
            else:
                l.append(i)
        l=l+l[-2:-n-1:-1]
        print(*l)
    for i in range(1,n):
        l=[]
        for j in range(n,0,-1):
            if j>i:
                l.append(j)
            else:
                l.append(i+1)
        l=l+l[-2:-n-1:-1]
        print(*l)

printingpattern(9)   