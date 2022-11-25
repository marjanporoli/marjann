list1=[]
list2=[]
n=int(input("enter the elements:"))
for i in range(0,n):
    list1.append(int(input()))
print("first list is:",list1)
num=int(input("enter the elements:"))
for i in range(0,num):
    list2.append(int(input()))
print("second list is:",list2)
sum1=0
sum2=0
for i in list1:
    sum1=sum1+i
print("sum of first list:",sum1)
for j in list2:
    sum2=sum2+j
print("sum of second list:",sum2)
if sum1==sum2:
    print("sum of two list are same")
else:
    print("sum of two list are not same")
