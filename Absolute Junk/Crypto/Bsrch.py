lst=[1,3,8,70,220,225,369,370,385,390,395,400]
mid=len(lst)//2 -1
def bsrch(mid,n):
	if n>lst[mid]:
		return bsrch(mid+1,n)
	elif n<lst[mid]:
		return bsrch(mid-1,n)
	else:
		print ("no. found with index no.",mid)
n= int(input("enter the no."))
b=bsrch(mid,n)