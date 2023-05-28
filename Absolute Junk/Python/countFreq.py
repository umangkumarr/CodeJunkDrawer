def count(s,ss):
    d=len(s)
    e,c=len(ss),0
    for i in range(d-e+1):
        if s[i:i+e]==ss:
            c+=1
    return c
print(count('caaab','aa'))
