
def counterGame(n):
    ss='{0:0b}'.format(n)
    a=ss.count('1')
    a=a+ss[::-1].index('1')-1
    return 'Richard' if a%2==0 else 'Louise'
    