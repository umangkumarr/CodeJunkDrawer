def strcal(t):
    m=[]
    for i in range(1,len(t)+1):
        l=[]
        for j in range(0,len(t)-i+1):
            f=t[j:i+j]
            l.append(f)
        s=l.copy()
        s=set(s)
        y=0
        for k in s:
            g=l.count(k)
            if g>y:
                y=g
        m.append(i*y)
    return max(m)
print(strcal('abcabcddd'))