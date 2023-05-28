
def equal(arr):
    mn=min(arr)
    dp=[0 for i in range(4)]
    for i in arr:
        for j in range(4):
            r=i-mn+j
            r=r//5 +(r%5)//2 +(r%5)%2
            dp[j]+=r
    return min(dp)

    