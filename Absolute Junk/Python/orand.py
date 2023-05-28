try:
    def subsets(s):
        sets = []
        for i in range(1 << len(s)):
            subset = [s[bit] for bit in range(len(s)) if is_bit_set(i, bit)]
            sets.append(subset)
        return sets
    def is_bit_set(num, bit):
        return num & (1 << bit) > 0
    from functools import reduce
    t=int(input())
    for er in range(t):
        n,m=map(int,input().split())
        nl=list(map(int,input().split()))
        ml=list(map(int,input().split()))
        if 0 in ml:
            ml.remove(0)
        if 0 in nl:
            nl.remove(0)
        ns=subsets(nl);ns.remove([])
        ms=subsets(ml);ms.remove([])
        n_or=[];m_and=[]
        for i in ns:
            n_or.append(reduce(lambda x,y:x|y,i))
        for j in ms:
            m_and.append(reduce(lambda x,y:x&y,j))
        m_and=set(m_and);n_or=set(n_or)
        a=[]
        for i in n_or:
            for j in m_and:
                a.append(i&j)
        a+=n_or
        # a=set(a)
        if 0 in a:
            print(len(a))
        else:
            print(len(a)+1)
except:
    pass