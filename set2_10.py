num=int(input())
b=1
c=[]
for i in range(1,6):
 b=i*num
 c=b.append(b)
print(*c)
