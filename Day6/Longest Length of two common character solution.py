string=input().strip()
reverse=string[::-1]
setu=set(string)
maxLength=[]
for i in setu:
    maxLength.append(abs(((string.find(i)))-((len(string)-1-reverse.find(i)))))
print(max(maxLength))    
