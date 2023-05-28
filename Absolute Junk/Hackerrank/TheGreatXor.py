
def theGreatXor(x):
    b=format(x,'b')[::-1]
    s=0
    for i in range(len(b)):
        if b[i]=='0':
            s+=2**i
    return s
print(theGreatXor(2))
