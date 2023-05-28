
import math
def encrypt(s):
    s=s.replace(' ','')
    rows=int(len(s)**0.5)
    column=math.ceil(len(s)**0.5)
    lst=[]
    for i in range(column):
        a=''
        for j in range(i,len(s),column):
            a=a+s[j]
        lst.append(a)
    print(*lst)

encrypt('haveaniceday')