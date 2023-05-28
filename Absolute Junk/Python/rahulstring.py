from collections import Counter
q=int(input())
for _ in range(q):
    a,b=[input() for __ in range(2)]
    ca=Counter(a.upper())
    cb=Counter(b)
    if all(x.lower() in a and (ca-cb)[x]==a.count(x.lower()) for x in (ca-cb).keys()):
        if (cb-ca)==Counter():
            print(1)
        else:
            print(0)
    else:
        print(0)