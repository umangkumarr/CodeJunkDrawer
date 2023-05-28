with open('r5.txt','r') as f:
    a=f.readlines()
for i in a:
    for k in i:
        h=ord(k)-65
        d=hex(h).encode()
        if len(d[2:])<2:
            print("0"+d[2:],end='')
        else:
            print(d[2:],end='')
    print()
