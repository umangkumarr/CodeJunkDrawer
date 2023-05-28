t=int(input())
for i in range(t):
    n,m,k= map(int,input().split())
    queries=[]
    for j in range(n):
        s,l=map(int,input().split())
        queries.append([s,'('])
        queries.append([l,')'])
    queries.sort()
    d=0
    count=0
    indx=0
    for j in range(len(queries)):
        if d==0:
            indx=j
            d+=1
        elif queries[j][1]=='(':
            d+=1
        else:
            d-=1
            if d==0:
                count+=queries[j][0]-queries[indx][0]
                indx=j+1
    print(f-count)

        
            

