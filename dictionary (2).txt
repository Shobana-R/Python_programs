''' create a dictionary with tuple-empid
emp_name are in a list'''

empid=(100,340,500,478,134,670)
names=['Vivan','Gopal','Vikram','Reena','Ravi','Ashish']
myDict={}
for var in range(len(empid)):
    myDict[empid[var]]=names[var]
print(myDict)
