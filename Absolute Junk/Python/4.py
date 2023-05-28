def solve(A,B):
    c=0
    for i in range(2,len(A)):
        j=0
        while (j+i)<len(A):
            m=max(A[j:j+i])
            r=(A[j]+A[j+i-1]-m)%B
            if B==0:
                c+=1
            j+=1
    return c%(10**9+7)
    