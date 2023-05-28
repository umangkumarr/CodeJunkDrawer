n, q, k = map(int, input().split())

# this will not pass the 2nd testcase
arr = list(map(int,input().split()))
l=r=k
temp = []
for i in range(q):
    temp.append(map(int, input().split()))

for a,b in temp[::-1]:
    if b >= l and a <= r:
        if a<l:
            l = a
        if b>r:
            r = b

print(sorted(arr[l:r+1])[k-l])
