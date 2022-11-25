list1=[]
list2=[]
n=int(input("enter the elements in first list:"))
for i in range(0,n):
    list1.append(int(input()))
print("first list is:",list1)
num=int(input("enter the elements in second list:"))
for i in range(0,num):
    list2.append(int(input()))
print("second list is:",list2)
len1=len(list1)
len2=len(list2)
print("output of a")
if len1==len2:
    print("two list are same length")
else:
    print("two list are not same")
print("output of b")
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
print("output of c")
for x in list1:
    for y in list2:
        if x==y:
            print(x,"is the common element in these two list")
    

