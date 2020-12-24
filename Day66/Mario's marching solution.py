I=input
I()
l=(list(map(int,I().split())))
H=L=0
for i in range(len(l)-1):
 if(l[i]>=l[i+1]):L+=1
 else:H+=1
print(H,L)