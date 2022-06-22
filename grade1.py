'''If the marks is between 90 to 100-A+ grade
If the marks is between 80 to 90-A grade
If the marks is between 70 to 80-B+ grade
If the marks is between 60 to 70-B grade
If the marks is between 50 to 60-C grade
else grade -F'''

grade=""
marks=int(input("Enter the marks "))
if(marks>=90 and marks<=100):
    grade="A+"
elif(marks>=80 and marks<=90):
    grade="A"
elif(marks>=70 and marks<=80):
    grade="B+"
elif(marks>=60 and marks<=70):
    grade="B"
elif(marks>=50 and marks<=60):
    grade="C"
else:
    grade="F"
print("The grade obtained is ",grade) 
