

def almostSorted(arr,n):
    arrsorted=sorted(arr)
    temparr=arr.copy()
    if arrsorted==arr:
        print("yes")
        return 0
    first=-1;last=-1   #these represent the first and last not equal indexes
    for i in range(n):
        if arrsorted[i]!=arr[i]:
            first=i
            break
    for i in range(n-1,0,-1):
        if arrsorted[i]!=arr[i]:
            last=i
            break
    temparr[first],temparr[last]=temparr[last],temparr[first]
    if temparr==arrsorted:
        print("yes\nswap",first+1,last+1)
    elif arrsorted[first:last+1]==arr[last:first-1:-1]:
        print("yes\nreverse",first+1,last+1)
    else:
        print("no")


almostSorted([1,5,4,3,2,6],6)



