n=int(input())
l=[]
for i in range(n):
  a=input()
  l.append(a)
for j in range(n):
  b=l[j].find(".")
  try:
    if b!=(len(l[j])-1) and b!=-1 and type(float(l[j]))==float:
      print("True")
    else:
      print("False")
  except:
    print("False")