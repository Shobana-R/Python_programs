print("Starting set: ")
lst1=[78,123,80,2,25]
lst2=[67,23,90,8,94]
myset=set()
myset.update(lst1,lst2)
print("The set is : ",myset)
print("Minimum number: ",min(myset))
print("Maximum number: ",max(myset))
print("Sum of the numbers: ",sum(myset))
print("Average: ",sum(myset)/len(myset))
print("The sorted set is : ",sorted(myset,reverse=True))
