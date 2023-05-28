

def nondivisblesubset(carr,k):
    carr=[i%k for i in carr]
    carr.sort(reverse=True)
    r=carr.count(0)
    c=0
    if r>1:
        carr=carr[:len(carr)-r+1]
        c+=1
    if k%2==0:
        l=k//2
    else:
        l=k//2+1
    for j in range(1,l):
        z=carr.count(j)
        x=carr.count(k-j)
        if z>=x: c+=z
        else: c+=x
    if k%2==0 and carr.count(k//2)>=1: c+=1
    return c
print(nondivisblesubset([19,10,12,10,24,25,22],4))

