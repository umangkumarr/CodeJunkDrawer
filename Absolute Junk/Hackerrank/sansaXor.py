
def sansaXor(arr):
    from functools import reduce
    if len(arr)%2==0:
        return 0
    xor=0
    i=(len(arr)//2)+1
    l=[arr[x] for x in range(0,len(arr),2)]
    return reduce(lambda a,b:a^b,l)
    