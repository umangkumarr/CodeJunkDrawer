def s(a,b):
    from collections import Counter,defaultdict
    di=defaultdict(lambda : [])
    for x in range(len(a)):
        if a.count(a[x])>1:
            di[a[x]].append(x)
    di=sorted(di.items(),key=lambda x:x[1][0])
    print(di)

from collections import Counter,defaultdict
s([1,1,1,2,3,4,5,2,3,4,5,2],2)
