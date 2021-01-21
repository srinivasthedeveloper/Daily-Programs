#Type 1
I=input
print(*[bin(int(I())).count('1')for i in '.'*int(I())],sep='\n')

#Type 2
input()
while 1:print(sum([0,1][b=='1']for b in bin(int(input()))))