n=int(input())
s=0
for i in range(n):
 t=input().count('/\\')
 s+=t
print(s)