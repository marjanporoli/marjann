string = str(input("Enter the string: "))
start=string[0]
end=string[-1]
result=end+string[1:-1]+start
print("the result is: ",result)
