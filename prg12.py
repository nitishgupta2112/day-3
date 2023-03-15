my_list = [9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result ={}
res=[]
for i in list_b:
    res.append((i,my_list.index(i)))
for i in res:
    if i in result:
        result[i]=result[i]+1
    else:
        result[i]=1

print(res)
print(result)

result1 =[((i,my_list.index(i))) for i in list_b]
print(dict(result1))