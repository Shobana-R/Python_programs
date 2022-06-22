'''Tax Calculation
Get Annual Income from User
Calculate Tax based on income
Upto 250000 no tax
240000 to 500000 -> 5 %
500000 to 1000000 -> 20 %
1000000 and above -> 30 %
'''
AnnIncome = int(input("Enter Annual Income"))
tax = 0
tax30 = 0
tax20 = 0
tax5 = 0
# tax Calculation
if(AnnIncome > 1000000):
	tax30 = (AnnIncome - 1000000) * 0.3
	tax20 = 100000
	tax5 = 12500
elif(AnnIncome > 500000):
	tax20 = (AnnIncome-500000) * 0.2
	tax5 = 12500
elif(AnnIncome > 250000):
	tax5 = (AnnIncome -250000) * 0.05
else:
	print("You have no tax this year")	

tax = tax30 + tax20 + tax5
print ("Total Tax: ",tax)


