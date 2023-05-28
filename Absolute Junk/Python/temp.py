t=int(input())
for _ in range(t):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort(); B.sort()

    if n==2:
        if B[0]-A[0]>0 and B[0]-A[1]>0:
            ans = min(B[0]-A[0],B[0]-A[1])
        else:
            ans = max(B[0]-A[0],B[0]-A[1])
            print(ans)
            continue
    if A[n-1]-B[n-2] == A[n-2]-B[n-3]:
        ans  = -A[n-1]+B[n-2]
    else:
        ans  = -A[n-3] + B[n-3]
    dd=100000000
    if A[n-2]-B[n-2] == A[n-3]-B[n-3]:
        dd  = -A[n-2]+B[n-2]
    
    

    print(min(ans,dd))