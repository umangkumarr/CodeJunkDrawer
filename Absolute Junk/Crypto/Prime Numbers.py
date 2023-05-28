import time
r=time.time()
lst=[i for i in range(2,1000)]
i=0
while i<len(lst):
	for k in lst:
		if k!=lst[i] and k%lst[i]==0:
			lst.remove(k)
	print(lst[i])
	i+=1
t=time.time()
print("Time taken : ",(t-r))
print("Total primes: ",len(lst))