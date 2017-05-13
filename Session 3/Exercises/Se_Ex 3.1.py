
clothes = ["T-Shirt", "Sweat", "Jeans"]


print ("==========================================")
print ("Add = C, Show = R, Insert = U, Delete = D")
print ("==========================================")

while True:
    action = input("Welcome to our shop, what do you want (C, R, U, D) ?")
    print(action)
    action = action.upper()

##    print ("Clothes in shop: ")
##    item_no = 1
##    for clothe in clothes:
##        print("{0}. {1}".format(item_no, clothe))
    
    if action == "C":
        item = input("Enter new item: ")
        clothes.append(item)
        
    elif action == "R":
        print(clothes)
        
    elif action == "U":
        item_no = int(input("Update new position: "))
        item_new = input("New item: ")
        clothes.insert(item_no, item_new)

    elif action == "D":
        item_no = int(input("Delete position: "))
        clothes.pop(item_no)

        
    print("Our item: ", clothes)
