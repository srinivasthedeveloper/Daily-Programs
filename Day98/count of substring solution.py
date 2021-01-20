#Type 1
s = input().lower()
text = input().lower()
print(len([x for x in text.split() if x.count(s)>0]))

#Type 2
s=input().lower().strip()
t=(input().lower().split())
c=0
for i in t:
    if(len(i)!=len("".join(i.split(s)))):
        c+=1
print(c)
