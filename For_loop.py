
# Write Python 3 code in this online editor and run it.

txt = input("Enter comma separated numbers: ")

x = txt.split(",")

print (x)

product = 1

for i in x:

    product = product * int(i)


print (product)
