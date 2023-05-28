n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
max=0
c=0
for i in range(n-1):
    for j in range(i+1,n):
        x,y=int(l[i],2),int(l[j],2)
        a=bin(x|y)
        d=a[2:].count('1')
        if d>max:
            max=d
            c=1
        elif d==max:
            c+=1
print(max)
print(c)