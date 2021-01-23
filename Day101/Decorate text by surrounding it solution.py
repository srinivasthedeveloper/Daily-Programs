w,s,n=input().split()
n=int(n)
t=len(w)+2+(n*2)
p=(s*t+"\n")*n
m=s*n+" "
print(p+w.join([m,m[::-1]])+"\n"+p)