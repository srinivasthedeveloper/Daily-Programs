#VERSION 2.0
I=input
c,n,d=[int(i) for i in I().split()]
g=I()
a='NOT'if sum([g.count(str(i)) for i in range(d+1)])<n else''
print(f"YOU_CAN{a}_MAKE_A_SOUP_IN_{d}_DAYS")


#VERSION 1.0
I=input
c,n,d=map(int,I().split())
l=I().replace('0',"")
c=0
for i in set(l):c+=(d%int(i))*l.count(i)
p="NOT"if(c<n)else""
print("YOU_CAN%s_MAKE_A_SOUP_IN_%d_DAYS"%("not",d))