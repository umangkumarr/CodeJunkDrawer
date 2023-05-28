
def substrings(n):
    l=len(n)
    s=0
    for i in range(0,l):
        s+=(int(n[i]*(l-i))*(i+1))%(10**9 +7)
    return s
print(substrings('5689'))
