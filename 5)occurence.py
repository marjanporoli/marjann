list=[]
n=int(input("enter the number of names: "))
for i in range(0,n):
    list.append(str(input()))
    print(list)
    count=0
for i in list:
 for j in i:
    if j=="a":
        count=count+1
print("count",count)
