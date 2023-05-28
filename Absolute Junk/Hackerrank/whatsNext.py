

def solve(A,B):
    res=0
    for size in range(2*B,len(A)+1):
        for i in range(len(A)-size+1):
            window=A[i:i+size]
            print(window)
            if sum((window.count(x)>=2) for x in set(window))==B:
                res+=1
    print(res)
solve([1,2,3,1,2,3],2)
