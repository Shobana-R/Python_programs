'''Get user input as comma seperated numbers and then multiply the numbers '''
txt=input("Enter comma seperated numbers:")
value=txt.split(",")
print("The numbers entered are:",(value))
product=1
for num in value:
    print("The number you have this time is ",num)
    product=product*int(num)
print("The product of all the numbers entered is:",product)
print("==========================================")
