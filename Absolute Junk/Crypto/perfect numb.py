def prft_no(n):
	s=0		#s=sum
	for i in range (1,n):
		if n%i==0:
			s+=i
	return s==n
print(prft_no(6))