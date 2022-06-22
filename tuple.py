'''Given: a tuple of numbers.Pickthe numbers from the tuple that satifies the following conditions:
value is lesser than 100,exactly divisible by 7 and 5.Store the resultin a list and print it out'''
tup1=(10,140,25,23,90,67,55,100,125,35,70,75)
lst1=[]
for x in tup1:
    if x<100 and x%5==0 and x%7==0:
        lst1.append(x)
print(tup1)
print("Result is",lst1)
