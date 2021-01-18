*n,=map(int,input())  #*n,=map(int,input()) is litrally act as n=list(map(int,input()))
s=input()
t=""
if(len(s)<len(n)):
    for i in n:
        print(s[i],end="")
else:
    s=s[:len(n)]+" "+s[len(n):].split()
    for i in range(len(s)):
    	for j in n:
    		t+=s[i][j]
	    t+=" "
	print(t.rstrip())