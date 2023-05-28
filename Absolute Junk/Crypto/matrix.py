n,m=map(int,input().split())
l=[]
for i in range(n):
  a=input()
  l.append(a)
q=zip(*l)
s=""
for j in q:
  s=s+"".join(j)
import re
z=re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',s)
print(z)