import itertools
k,m=map(int,input().split())
l=[]
for i in range(0,k):
  a=list(map(int,input().split()))[1:]
  l.append(a)
d=map(lambda x:sum(i*i for i in x)%m,itertools.product(*l))
print(max(d))