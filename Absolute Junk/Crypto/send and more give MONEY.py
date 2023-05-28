#send + more = money
#solution
import random
while True:
	s=random.randint(0,9)
	e=random.randint(0,9)
	n=random.randint(0,9)
	d=random.randint(0,9)
	m=random.randint(1,9)
	o=random.randint(0,9)
	r=random.randint(0,9)
	y=random.randint(0,9)
	k= s*1000+e*100+n*10+d
	a=m*1000+o*100+r*10+e
	p=m*10000+o*1000+n*100+e*10+y
	if (k+a)==p and s!=e!=n!=d!=m!=o!=r!=y:
		print(s,e,n,d,m,o,r,y)