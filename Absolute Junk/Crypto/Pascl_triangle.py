n=int(input("no. of rows"))
t=[1]
y=[0]
for x in range(0,n):
	for j in range(0,2*(n-x)):
		print(end=" ")
	t=[l+r for l,r in zip(t+y,y+t)]
	print(" ".join(map(str,t)))