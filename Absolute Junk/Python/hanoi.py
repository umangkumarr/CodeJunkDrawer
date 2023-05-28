n=int(input())
def transfer(n,frm,to,t):
    if n>0:
        transfer(n-1,frm,t,to)
        print(f'Move disk {n} from {frm} to {to}')
        transfer(n-1,t,to,frm)
transfer(n,'L','R','C')