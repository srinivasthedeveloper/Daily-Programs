#TYPE 1
s=["AG","UB","OZ","UEM"]
n=int(input())
t=s[n%4]
while n>3:n//=4;t+=s[n%4]
print(t[::-1])


#TYPE 2
n=int(input())
s=""
while n:s=["GA","BU","ZO","MEU"][n%4]+s;n//=4
print(s if s else"GA")