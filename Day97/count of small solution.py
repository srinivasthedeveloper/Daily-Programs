#Type 1
print(sum([1 for i in input() if(i.islower())]))

#Type 2
print(len(list(filter(str.islower,input()))))