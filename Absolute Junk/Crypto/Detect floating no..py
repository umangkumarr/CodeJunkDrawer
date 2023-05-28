import re
n=int(input())
l=[]
for i in range(0,n):
  a=input()
  l.append(a)
for j in range(0,n):
  if type(float(l[j]))==float and bool(re.search(r".",l[j]))==True and bool(re.match(r".",reversed(l[j])))==False:
    print("True")
  else:
    print("False")