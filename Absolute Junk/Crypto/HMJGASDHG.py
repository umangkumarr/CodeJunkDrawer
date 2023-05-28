def l(a,b):
  s=''
  while a and b:
    if a+b<b+a:
      s+=a[0]
      a=a[1:]
    else:
      s+=b[0]
      b=b[1:]
  return s+a+b
n=int(input())
for k in range(n):
  a=input()
  b=input()
  print(l(a,b))