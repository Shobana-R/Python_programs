'''Adding items into Shopping cart'''
print("Shopping cart")
item_list=[]
while(True):
    item=input("Enter the item name: ")
    qty=int(input("Enter quantity: "))
    each_item=[]
    each_item.append(item)
    each_item.append(qty)
    item_list.append(each_item)
    more=input("Do you want to continue(yes/no):")
    if(more=="no"):
        break 
print("you have purchased ",item_list)

'''i = 0

while(True):

    i = i + 1
    if(i == 5):
        continue
    
    if(i == 10):
        break
    print (i)
'''
