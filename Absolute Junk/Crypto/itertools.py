s=input()
k=int(input())
n=len(s)//k
import textwrap
l=textwrap.wrap(s,n)
for i in l:
  d=list(i[::-1])
  g=set(i)
  for t in g:
    for e in range(1,i.count(t)):
      d.remove(t)
  print(''.join(d[::-1]))