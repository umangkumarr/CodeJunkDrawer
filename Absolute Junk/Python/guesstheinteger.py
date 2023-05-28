t=int(input())
for i in range(t):
    l=[];r=[]
    n=int(input())
    for j in range(n):
        inp=input()
        if inp[0]=='L':
            l.append(int(inp[2:]))
        else:
            r.append(int(inp[2:]))
    l.sort();r.sort()
    print(l)
    print(r)
    if len(l)>0 and len(r)>0 and (l[0]-r[-1])>0 :
        print(l[0]-r[-1]-1)
    else:
        print(-1)