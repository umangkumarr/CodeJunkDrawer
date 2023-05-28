n=""
a=""
for r in range(0,26):
    for i in range(0,len(n)):
        d=ord(n[i])+r
        if d>90:
            a+=chr(d-26)
        else:
            a+=chr(d)
    print(a)
    a=""
    print()
    print()

