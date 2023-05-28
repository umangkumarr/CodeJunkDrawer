for i in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    l=[]
    for i in range(n):
        c=0
        for j in range(i+1,n):
            if h[j]==h[i]:
                c+=1
            elif h[j]>h[i]:
                break
        for k in range(i-1,-1,-1):
            if h[k]==h[i]:
                c+=1
            elif h[k]>h[i]:
                break
        l.append(c)
    print(*l)