#X Odd Integers - Subarrays
def xOddIntegersSubarrays():
	n,o=map(int,input("Enter Number of elements(space)odd count:-").split())
	l=list(map(int,input("Enter the elements:- ").split()))
	tl=[]
	counts=0
	for i in range(len(l)):
		for j in range(len(l)):
			if(l[i:i+j+1] not in tl):
				tl.append(l[i:i+j+1])
	for i in tl:
		s=sum([1 for j in i if j%2==1])
		if(s==o):
			counts+=1
	print("Number of counts is:-",counts)