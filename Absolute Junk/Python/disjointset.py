def make(n):
    parent=[i for i in range(n)]
    size=[1]*n

def find(a):
    if a==parent[a]:
        return a
    parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if size[a]<size[b]:
            swap(a,b)
        parent[b]=a
        size[a]+=size[b]

