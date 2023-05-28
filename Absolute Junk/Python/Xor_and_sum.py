
def xorAndSum(a, b):
    x=int(a,2)
    y=int(b,2)
    s=0
    for i in range(314160):
       s+=(x^(y<<i))
    return s%(10**9 +7) 
    