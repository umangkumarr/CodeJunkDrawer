t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    s3=input()
    x=s1.count('X')+s2.count('X')+s3.count('X')
    o=s1.count('O')+s2.count('O')+s3.count('O')
    _=9-x-o
    x_win=0
    o_win=0
    if x==o or x==o+1:
        if s1.count('X')==3:
            x_win=1
        elif s1.count('O')==3:
            o_win=1
        if s2.count('X')==3:
            x_win=1
        elif s2.count('O')==3:
            o_win=1
        if s3.count('X')==3:
            x_win=1
        elif s3.count('O')==3:
            o_win=1
        if s1[0]==s2[0]==s3[0]=='X':
            x_win=1
        elif s1[0]==s2[0]==s3[0]=='O':
            o_win=1
        if s1[1]==s2[1]==s3[1]=='X':
            x_win=1
        elif s1[1]==s2[1]==s3[1]=='O':
            o_win=1
        if s1[2]==s2[2]==s3[2]=='X':
            x_win=1
        elif s1[2]==s2[2]==s3[2]=='O':
            o_win=1
        if s1[0]==s2[1]==s3[2]=='X':
            x_win=1
        elif s1[0]==s2[1]==s3[2]=='O':
            o_win=1
        if s1[2]==s2[1]==s3[0]=='X':
            x_win=1
        elif s1[2]==s2[1]==s3[0]=='O':
            o_win=1
        
        if x_win==1 and o_win==1:
            print(3)
            continue
        elif o_win==1:
            if x!=o:
                print(3)
                continue
            else:
                print(1)
                continue
        elif x_win==1:
            if x==o:
                print(3)
                continue
            else:
                print(1)
                continue
        else:
            if _>0:
                print(2)
                continue
            else:
                print(1)
                continue
    else:
        print(3)
        continue