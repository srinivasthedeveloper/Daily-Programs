#Type 1
c,n=map(int,input().split())
l=[]
for i in range(n):
	t=list(map(int,input().split()))
	l.append(t)

#Type 2	
l=sorted(l,key=lambda l:l[1],reverse=True)
l=sorted(l,key=lambda l:l[0])
m=[0]*len(l)
for i in range(len(l)):
	t=c
	for j in l[i:]:
		if(j[0]<=t):
			m[i]+=j[1]
			t-=j[0]