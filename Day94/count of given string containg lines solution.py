def a():
	c=0
	s=input().lower().strip()
	n=int(input())
	l=[input().lower() for i in range(n)]
	for i in range(n):
			t=list(l[i])
			try:
				for j in s:
					t.remove(j)
				if(len(t)+len(s)==len(l[i])):
					c+=1
			except Exception:
				print("",end="")
	print(c)