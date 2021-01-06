n,c=map(eval,input().split())
if(c=='N'):
	for i in range(n):
		for j in range(n):
			if(j==0 or j==n-1):
				print('N',end="")
			elif(j==i):
				print('N',end="")
			else:
				print('-',end="")
		print()
elif(c=='Y'):
	for i in range(n):
		for j in range(n):
			if(i<=n//2):
				if(j==0+i or j==n-i-1):
					print("Y",end="")
				else:
					print("-",end="")
			elif(i>n//2):
				if(j==n//2):
					print("Y",end="")
				else:
					print("-",end="")
		print()
else:
	print("Invalid")