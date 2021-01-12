n=int(input())
powers=[2**i for i in range(1,n)]
if n in powers:
	print(1)
else:
	for i in range(len(powers)):
		if(powers[i]>n):
			print(2*(n-powers[i-1])+1)
		exit()