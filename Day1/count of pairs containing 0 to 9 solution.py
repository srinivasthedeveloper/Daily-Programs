'''
for i in range(n-1):
	for j in range(i+1,n):
		if("0123456789" in ''.join(sorted(set(l[i]+l[j])))):
			counts+=1

n=int(input())
l=list(map(str,input().split()))
counts=sum([1 for i in range(n-1) for j in range(i+1,n) if("0123456789" in ''.join(sorted(set(l[i]+l[j]))))])
print(counts)
'''
from itertools import combinations
n=int(input())
l=list(map(str,input().split()))
counts=sum([1 for item in combinations(l,2) if("0123456789" in ''.join(sorted(set(''.join(item)))))])
print(counts)
