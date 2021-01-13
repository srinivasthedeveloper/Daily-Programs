r=int(input())
g=int(input())
b=int(input())
print("#"+(str(hex(r))[2:].zfill(2)+str(hex(g))[2:].zfill(2)+str(hex(b))[2:].zfill(2)).upper())