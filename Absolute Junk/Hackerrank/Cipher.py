def cipher(n,k,s):
    s=list(map(int,s))
    a=0;l=[]
    for i in range(n):
        l.append(a^s[i])
        a^=l[-1]
        if i>=k-1:
            a^=l[i-k+1]
    return l
a='1110100110'
print(*cipher(7,4,a),sep='')
-------------------------------------------------------------------------------------
from functools import reduce
def cipher(k,s):
    l=[0]*(k-1)
    for i in range(len(s)-k+1):
        x=int(s[i])^reduce(lambda a,b:a^b,l[i:])
        l.append(x)
    print(len(l))
    return l[:k-len(l)-2:-1]
a='1110011011'
print(cipher(3,a[::-1]))