def canPartition(nums):
    if sum(nums) % 2: return False
    def dfs(n, target):
        if not target: return True
        if n == 1 or target < 0: return False
        return dfs(n - 1, target - nums[n - 1]) or dfs(n - 1, target)
    return dfs(len(nums), sum(nums) // 2)
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=sorted(list(map(int,input().split())),reverse=True);r=0
    if arr[0]>=k:
        c=1;s=0
        for j in arr[1:]:
            s+=j
            c+=1
            if s>=k:
                r=1
                print(c)
                break
        if r==1:
            continue
        if c<=1:
            print(-1)
    elif sum(arr)>=2*k:
        if sum(arr)==2*k:
            if canPartition(arr):
                print(len(arr))
                continue
            else:
                print(-1)
                continue
        else:
            a=[];s=0
            for j in range(n):
                s+=arr[j]
                a.append(arr[j])
                if s>=2*k:
                    break
            print(a,s)
            if canPartition(a):
                print(len(a))
                continue
            a1=[a[0]];s1=a[0]
            for qw in range(j,0,-1):
                s1+=a[qw]
                a1.append(a[qw])
                if s1>=k:
                    break
            print(a1,s)
            s2=0;a2=[]
            for l in range(qw-1,0,-1):
                s2+=a[l]
                a2.append(a[l])
                if s2>=k:
                    break
            print(a2,s2)
            if s2>=k:
                print(len(a1)+len(a2))
                continue
            else:
                for f in range(j+1,n):
                    s2+=arr[f]
                    a2.append(arr[f])
                    if s2>=k:
                        break
                if s2>=k:
                    print(len(a1)+len(a2))
                else:
                    print(-1)