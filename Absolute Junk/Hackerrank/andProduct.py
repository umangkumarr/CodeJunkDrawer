# def andProduct(a,b):
#     l=len("{0:b}".format(b))-1
#     if a<(2**l):
#         return 0
#     elif a==2**l or a==2**l+1:
#         return 2**l
#     else:
#         return a
# print(andProduct(12,15))

for i in range(10,50):
    print(i,'{0:b}'.format(i))