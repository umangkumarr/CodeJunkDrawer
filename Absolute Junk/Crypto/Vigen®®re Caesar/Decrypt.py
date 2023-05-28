ltr="DPRYEVNTNBUKWWBT"
kyw="KING"
for i in range(0,len(ltr)):
    pstn=i%len(kyw)
    c,d=ord(ltr[i]),ord(kyw[pstn])
    if d<c:
        print(chr(c-d+65),end="")
    else:
        f=26-(d-c)
        print(chr(65+f),end="")