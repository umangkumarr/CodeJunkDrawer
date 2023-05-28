def minsubarray(arr,k):
    # arr.sort()
    start=0;ansEnd=0;ansStart=0;currSum=0;minLen=len(arr)
    f=False
    for i in range(len(arr)+1):
        while currSum>=k:
            f=True
            currSum-=arr[start]
            if i-start<=minLen:
                minLen=i-start
                ansEnd=i
                ansStart=start
            start+=1
        if i<len(arr):
            currSum+=arr[i]
    if f:
        return minLen,arr[ansStart:ansEnd]
    else:
        return -1,[]
t=int(input())
for l in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    minl,ar1=minsubarray(a,k)
    if minl==-1:
        print(minl)
        continue
    arr=[];j=0
    for i in range(len(a)):
        if a[i]!=ar1[j]:
            arr.append(a[i])
        else:
            j+=1
    minl2,ar2=minsubarray(arr,k)
    if minl2==-1:
        print(-1)
        continue
    print(minl2+minl)