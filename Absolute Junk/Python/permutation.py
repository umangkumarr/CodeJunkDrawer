from itertools import permutations
n=int(input())
lt=list(map(int,input().split()))
c=lt.count(0)
for i in range(c):
    lt.remove(0)
l=list(permutations(range(1,n+1)))
for i in range(len(l)):
    l[i]=list(l[i])
def trim(x):
    for i in range(len(x)):
        for j in range(n-1,-1,-1):
            if x[i][j] not in lt:
                x[i].remove(x[i][j])
    return x
k=trim(l)
print(k)
