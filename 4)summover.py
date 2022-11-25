list=[]
num=int(input("enter the number: "))
for i in range(0,num):
    list.append(int(input()))
print(list)
result=[]
for i in list:
  if i > 100:
    result.append("over")
  else:
    result.append(i)
  print(result)

