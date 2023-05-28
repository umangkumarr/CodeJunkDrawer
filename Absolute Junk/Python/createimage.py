import math
from PIL import Image
pi=3.14159
img=Image.new(mode='RGB',size=(8,8),color=(255,255,255))
# img.show()
img.save("/Users/umangkumar/Desktop/white_image.jpg")
pixel=img.load()
print(list(pixel[1,3]))
def t_value(i,j):
    if i==0:
        return 8**(-0.5)
    else:
        return 0.5*(math.cos(pi*(2*j +1)*i/16))

def multiply(l1,l2):
    mul=[[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            s=0
            for k in range(8):
                s+=l1[i][k]*l1[k][j]
            mul[i][j]=s
    return mul

def transform():
    t=[[0 for i in range(8)] for k in range(8)]
    for i in range(8):
        for j in range(8):
            t[i][j]=t_value(i,j)
    return t

r=[[0 for i in range(8)] for j in range(8)]
b=r.copy()
g=r.copy()
for i in range(8):
    for j in range(8):
        r[i][j],b[i][j],g[i][j]=img.getpixel((i,j))

trans=transform()
rdct=multiply(multiply(trans,r),trans)
bdct=multiply(multiply(trans,b),trans)
gdct=multiply(multiply(trans,g),trans)

for i in range(8):
    for j in range(8):
        pixel[i,j]=(int(rdct[i][j]),int(bdct[i][j]),int(gdct[i][j]))

img.show()

            