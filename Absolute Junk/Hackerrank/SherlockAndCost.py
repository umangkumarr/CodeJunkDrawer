
def cost(B):
    low=0;high=0
    for i in range(1,len(B)):
        hl=abs(B[i-1]-1)
        lh=abs(1-B[i])
        hh=abs(B[i-1]-B[i])
        low_nxt=max(low,high+hl)
        hi_nxt=max(low+lh,high+hh)
        high=hi_nxt
        low=low_nxt
    return max(high,low)
