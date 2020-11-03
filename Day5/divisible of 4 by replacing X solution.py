number=input().strip()
print([(number[:-1]+str(i)) for i in [0,2,4,6,8] if(int(number[-2]+str(i))%4==0)])
