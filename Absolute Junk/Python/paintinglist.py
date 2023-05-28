n=11
parent=[i for i in range(n+1)]
answer=[0 for i in range(n+1)]
def find_set(a):
    if a==parent[a]:
        return a
    parent[a]=find_set(parent[a])
    return parent[a] 
def solve(n,queries):
    for i in queries[::-1]:
        l=i[0];r=i[1];c=[2]
        x=find_set(l)
        while x<=r:
            print(x)
            answer[x]=c
            parent[x]=x+1
            x=find_set(x)
    return answer
q=[[0,4,1],[5,10,1]]
print(solve(n,q))
