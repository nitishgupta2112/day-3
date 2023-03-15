str1 = list(map(int,input().split(",")))
num1=sum(str1[:str1.index(5)])+sum(str1[str1.index(8)+1:])
res = str1[str1.index(5):str1.index(8)+1]
num2=""
for i in res:
    num2+=str(i)
print(int(num2)+num1)

