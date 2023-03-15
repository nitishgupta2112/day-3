s= input().split(",")
string=[]
digits=[]
for i in s:
    s1,n=i.split(":")
    string.append(s1)
    digits.append(n)
def rotate(st,no):
    no=str(no)
    s=0
    for i in no:
        s+=int(i)**2
    if s%2==0:
        return st[-1]+st[:-1]
    else:
        return st[2:]+st[:2]
for i in range(len(digits)):
    print(rotate(string[i],digits[i]))
