n=int(input())
List=[list(map(int,input().split())) for i in range(n)]
listSum=[]
Index=[]
counts=0
for i in range(n-2):
	for j in range(n-2):
		listSum.append(List[i][j]+List[i][j+1]+List[i][j+2]+List[i+1][j+1]+List[i+2][j]+List[i+2][j+1]+List[i+2][j+2])
		print("\n",List[i][j],List[i][j+1],List[i][j+2],"\n  ",List[i+1][j+1],"-->",listSum[counts],"\n",List[i+2][j],List[i+2][j+1],List[i+2][j+2])
		counts+=1
		Index.append(str(i)+str(j))
t=Index[listSum.index(max(listSum))]
i,j=map(int,list(t))
print("\n",List[i][j],List[i][j+1],List[i][j+2],"\n  ",List[i+1][j+1],"-->",max(listSum),"\n",List[i+2][j],List[i+2][j+1],List[i+2][j+2])
