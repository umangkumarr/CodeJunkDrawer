# The Coin Change Problem

# recursive approch
def count(n,m,c):
    if n==0:
        return 1
    if n<0:
        return 0
    if m<=0 and n>=1:
        return 0
    return count(c,m-1,n) + count(c,m,n-c[m-1])

#bottom to top approch

def ways_count(n,m,c):

    ways_lst=[[0 for x in range(m)] for i in range(n+1)] #intial ways are zero
    
    for i in range(m):
        ways_lst[0][i]=1 #for 0 coins number of ways will be 1
    for i in range(1,n+1):
        for j in range(m):
            #solution including coin c[j]
            x=ways_lst[i-c[j]][j] if i-c[j]>=0 else 0
            #solution excluding coin c[j]
            #this transverse the count ways to this number to take count of total ways excluding this
            y= ways_lst[i][j-1] if j>0 else 0

            ways_lst[i][j]=x+y
    return ways_lst[n][m-1]

coin_arr=list(map(int,input().split()))
n=int(input())
print(ways_count(n,len(coin_arr),coin_arr))
