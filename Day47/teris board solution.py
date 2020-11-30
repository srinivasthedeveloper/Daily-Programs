r=sum([input()=='#'*10 for i in range(16)])
print((r+4*(r>3))*100)