#Python type1
print(*[chr(219-ord(i))for i in input()],sep="")

#python type 2
print(''.join([chr(219-ord(i))for i in input()]))