n=int(input())
def year(n):
  a=False
  if n%4==0:
    a=True
    if n%100==0 and n%400!=0:
      a=False
  return a
print(year(n))