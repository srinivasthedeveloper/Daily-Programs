string=input("Enter some value:-").strip()
orginal=string
temp=string[::-1]
counts=0
for i in range(1,len(orginal)):
        if(string==string[::-1]):
                break
        string=orginal
        string=temp[:i]+string
        #print(string) #visualize process
        counts+=1
print("I made it as a palindrome :-",string)
print(counts)
