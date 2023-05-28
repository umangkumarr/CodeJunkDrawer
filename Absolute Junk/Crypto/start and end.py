s=input()
k=input()
l=[]
r=False
for i in range(len(s)-len(k)+1):
  if k==s[i:i+len(k)]:
    r=True
    l.append((i,i+len(k)-1))
if r==True:
  for i in l:
    print(i)
else:
  print((-1,-1))