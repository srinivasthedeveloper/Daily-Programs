#TYPE 1
s=input()
t=s.count('0')
t+=s.count('6')
t+=s.count('9')
t+=(s.count('8')*2)
print(t)

#TYPE 2
s = input()
d={'0':1,'6':1,'8':2,'9':1}
print(sum(d.get(i,0) for i in s))
