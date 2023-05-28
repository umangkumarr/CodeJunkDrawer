l=[]
for i in range(0,64):
    l.append(str(1<<i))

def solve(a,b):
    count=0
    a1=0
    b1=0
    while a1<len(a) and b1<len(b):
        if a[a1]==b[b1]:
            b1+=1
            count+=1
        a1+=1
    return len(a) - 2*count + len(b)

t=int(input())
for _ in range(t):
    n=input()
    ans = len(n) + 1
    for  i in l:
        ans= min(ans,solve(n,i))
    print(ans)
