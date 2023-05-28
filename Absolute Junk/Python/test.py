import math
def digit_sum(n,i):
    return 0
    rem = n%i
    div = n//i
    # print(div)
    power = 0
    if div not in [0,1]:
        power = math.log(div)/math.log(i)
    pp=math.pow(i,power)
    div-=pp
    return div + rem -1

for i in range(2,100):
    n=i
    ans=0
    while n:
        ans+= n%5
        n//=5
    print([ans,digit_sum(i,5)],i, end='\n')