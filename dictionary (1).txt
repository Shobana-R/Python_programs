'''Create a dict having the values as list .Iterate and findthe sum,min,max,avg'''
dict1={100:[56,129],250:[65,67,78,90],350:[32,10,8,5]}
list1=[]
for key in dict1:
    valueStr=""
    for value in dict1[key]:
        valueStr=valueStr+str(value)+" "
    print("key is ",key," value is",valueStr)
    list1.extend(dict1[key])
print("Total:", sum(list1))
print("Maximum",max(list1))
print("Minimum",min(list1))
print("Average ",sum(list1)/len(list1))
