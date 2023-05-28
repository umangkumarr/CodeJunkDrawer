
def flippingBits(n):
    a='{:032b}'.format(n)
    return int(''.join([str(int(x)^1) for x in a]),2)
