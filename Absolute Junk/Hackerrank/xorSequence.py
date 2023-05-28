from functools import reduce
def index_val(n):               #values at  index n
    a=n%8
    if a==0 or a==4:            
        return n
    elif a==1 or a==5:
        return 1
    elif a==2 or a==6:
        return n+1
    elif a==3 or a==7:
        return 0
def xor_value(r):
    x=0
    for i in range(r+1):
        x^=index_val(i)
    return x%(10**9+7)      #analyzing xor values
for i in range(30):
    print(i,end=',')
print()
for i in range(30):
    print(xor_value(i),end=',')

-----------------------------------------------------------------------------------------
#program start
#!/bin/python3

from functools import reduce
def xor_val(n):
    a=n%8
    if a==1 or a==0:
        return n
    elif a==2 or a==3:
        return 2
    elif a==4 or a==5:
        return n+2
    elif a==6 or a==7:
        return 0
def xorSequence(l,r):
    return xor_val(r)^xor_val(l-1)
    
q = int(input())
for q_itr in range(q):
    lr = input().split()
    l = int(lr[0])
    r = int(lr[1])
    print(xorSequence(l, r))