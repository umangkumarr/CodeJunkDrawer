n="THESUNANDTHEMOON"
kyw="KING"
for i in range(0,len(n)):
    pstn=i%len(kyw)
    c,d=ord(n[i]),ord(kyw[pstn])
    if d+(c-65)<=90:
        print(chr(d+(c-65)),end="")
    else:
        print(chr((d+(c-65))-26),end="")
    


# abc aab cab
# abc

# a b c a b c a b c
# a b c a a b c a b
 
# A B C 
# B C A 
# C A B

# a c c a b a c b a
# acc aba cba