def nn(arr):
    from functools import reduce
    a=reduce(lambda y,b :y^b,arr)
    print(a)
    a=a<<(len(arr)-1)
    print(a)
nn([1,2,3,4])