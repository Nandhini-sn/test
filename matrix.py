input1=input().split()
n=int(input1[0])
m=int(input1[1])

mat=[]
for i in range (0,n):
    l=list(map(int,input().split()))
    mat.append(l)

for i in mat:
    print(i)
