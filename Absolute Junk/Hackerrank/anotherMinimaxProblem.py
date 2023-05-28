

from itertools import permutations
def anotherMinimaxProblem(a):
    s=list(permutations(a))
    mn=[]
    for i in s:
        m=[]
        for j in range(len(i)-1):
            m.append(i[j]^i[j+1])
        mn.append(max(m))
    return min(mn)
print(anotherMinimaxProblem(list(map(int,input().split()))))

