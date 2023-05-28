def solve(A):
    from collections import defaultdict,Counter
    a=list(set(A));c=0;l=[]
    for i in a:
        if A.count(i)>2:
            c+=1
    if c==0:
        return 0
    for i in range(len(A)):
        if A.count(A[i])>2:
            l.append(i)
    l.sort()
    mn=10**6
    for i in range(len(l)-c*2,len(l)+1):
        for j in range(len(l)-i):
            tl=A[:l[j]]+A[l[j+i-1]+1:]
            d=Counter(tl)
            if max(d.values())<3:
                print(tl)
                if mn>(abs(l[j]-l[j+i-1])):
                    mn=abs(l[j]-l[j+i-1])
        if mn!=10**6:
            return mn+1
print(solve([2,1,2,1,1,2,1,2]))